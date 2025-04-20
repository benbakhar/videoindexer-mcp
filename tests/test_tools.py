import unittest
from unittest.mock import patch, MagicMock
from src.tools import vi_create_prompt_content, vi_get_prompt_content
from src.services.videoindexer import ModelName, PromptStyle


class TestVideoIndexerTools(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.valid_params = {
            "location": "test-location",
            "accountId": "test-account",
            "videoId": "test-video"
        }

    def test_missing_required_params(self):
        """Test handling of missing required parameters."""
        required_params = ["location", "accountId", "videoId"]

        for param in required_params:
            invalid_params = self.valid_params.copy()
            invalid_params[param] = ""

            with self.assertRaises(ValueError):
                vi_create_prompt_content(**invalid_params)

            with self.assertRaises(ValueError):
                vi_get_prompt_content(**invalid_params)

    @patch('src.tools.get_access_token')
    def test_invalid_model_name(self, mock_get_token):
        """Test handling of invalid model name."""
        invalid_params = {
            **self.valid_params,
            "modelName": "InvalidModel"
        }

        with self.assertRaises(ValueError) as context:
            vi_create_prompt_content(**invalid_params)
        self.assertIn("Invalid model name", str(context.exception))

    @patch('src.tools.get_access_token')
    def test_invalid_prompt_style(self, mock_get_token):
        """Test handling of invalid prompt style."""
        invalid_params = {
            **self.valid_params,
            "promptStyle": "InvalidStyle"
        }

        with self.assertRaises(ValueError) as context:
            vi_create_prompt_content(**invalid_params)
        self.assertIn("Invalid prompt style", str(context.exception))

    @patch('src.tools.get_access_token')
    @patch('src.tools.VideoIndexerService')
    def test_vi_create_prompt_content(self, mock_service, mock_get_token):
        """Test vi_create_prompt_content tool."""
        mock_get_token.return_value = "test_token"
        mock_instance = mock_service.return_value
        mock_instance.create_prompt_content.return_value = "Job started successfully"

        # Test with required parameters only
        result = vi_create_prompt_content(**self.valid_params)
        self.assertEqual(result, "Job started successfully")

        # Test with all parameters
        full_params = {
            **self.valid_params,
            "modelName": "GPT4",
            "promptStyle": "Summarized"
        }
        result = vi_create_prompt_content(**full_params)
        self.assertEqual(result, "Job started successfully")

    @patch('src.tools.get_access_token')
    @patch('src.tools.VideoIndexerService')
    def test_vi_get_prompt_content(self, mock_service, mock_get_token):
        """Test vi_get_prompt_content tool."""
        mock_get_token.return_value = "test_token"
        mock_instance = mock_service.return_value
        mock_instance.get_prompt_content.return_value = {
            "status": "Succeeded",
            "prompt": "Test prompt"
        }

        result = vi_get_prompt_content(**self.valid_params)
        self.assertEqual(result["status"], "Succeeded")
        self.assertEqual(result["prompt"], "Test prompt")


if __name__ == '__main__':
    unittest.main()
