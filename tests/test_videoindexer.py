import unittest
import httpx
from unittest.mock import patch, MagicMock
from src.services.videoindexer import VideoIndexerService, PromptContentParams, ModelName, PromptStyle, HttpMethod


class TestVideoIndexerService(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.access_token = "test_token"
        self.service = VideoIndexerService(self.access_token)
        self.base_params = PromptContentParams(
            location="test-location",
            account_id="test-account",
            video_id="test-video"
        )

    def test_initialization(self):
        """Test service initialization."""
        self.assertIsInstance(self.service, VideoIndexerService)
        self.assertEqual(self.service.access_token, self.access_token)

        # Test initialization with empty token
        with self.assertRaises(ValueError):
            VideoIndexerService("")

    @patch('httpx.Client')
    def test_create_prompt_content(self, mock_client):
        """Test create_prompt_content method."""
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_response.text = "Job started"
        mock_response.raise_for_status.return_value = None
        mock_client.return_value.__enter__.return_value.post.return_value = mock_response

        # Test valid cases
        # Test with basic parameters
        result = self.service.create_prompt_content(self.base_params)
        self.assertIn("Job started", result)

        # Test with model name and prompt style
        params_with_options = PromptContentParams(
            location="test-location",
            account_id="test-account",
            video_id="test-video",
            model_name=ModelName.GPT4,
            prompt_style=PromptStyle.Summarized
        )
        result = self.service.create_prompt_content(params_with_options)
        self.assertIn("Job started", result)

        # Test parameter validation through public method
        invalid_params = [
            PromptContentParams(
                location="", account_id="test", video_id="test"),
            PromptContentParams(
                location="test", account_id="", video_id="test"),
            PromptContentParams(
                location="test", account_id="test", video_id="")
        ]

        for params in invalid_params:
            with self.assertRaises(ValueError):
                self.service.create_prompt_content(params)

    @patch('httpx.Client')
    def test_get_prompt_content(self, mock_client):
        """Test get_prompt_content method."""
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "Succeeded", "prompt": "Test prompt"}
        mock_response.raise_for_status.return_value = None
        mock_client.return_value.__enter__.return_value.get.return_value = mock_response

        # Test valid case
        result = self.service.get_prompt_content(self.base_params)
        self.assertEqual(result["status"], "Succeeded")
        self.assertEqual(result["prompt"], "Test prompt")

        # Test parameter validation through public method
        invalid_params = [
            PromptContentParams(
                location="", account_id="test", video_id="test"),
            PromptContentParams(
                location="test", account_id="", video_id="test"),
            PromptContentParams(
                location="test", account_id="test", video_id="")
        ]

        for params in invalid_params:
            with self.assertRaises(ValueError):
                self.service.get_prompt_content(params)

    @patch('httpx.Client')
    def test_http_error_handling(self, mock_client):
        """Test HTTP error handling."""
        error_cases = [
            (400, "Bad request"),
            (401, "Unauthorized"),
            (404, "not found"),
            (409, "conflict")
        ]

        mock_request = MagicMock()
        for status_code, expected_message in error_cases:
            # Mock error response
            mock_response = MagicMock()
            mock_response.status_code = status_code
            mock_response.text = "Error details"
            mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
                "Error", request=mock_request, response=mock_response
            )
            mock_client.return_value.__enter__.return_value.get.return_value = mock_response

            with self.assertRaises(ValueError) as context:
                self.service.get_prompt_content(self.base_params)
            self.assertIn(expected_message, str(context.exception))


if __name__ == '__main__':
    unittest.main()
