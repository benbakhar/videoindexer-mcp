from typing import Optional, Dict, Any, Literal
from dataclasses import dataclass
import httpx
from enum import Enum


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"


class ModelName(Enum):
    Llama2 = "Llama2"
    Phi2 = "Phi2"
    Phi3 = "Phi3"
    Phi3_5 = "Phi3_5"
    GPT3_5Turbo = "GPT3_5Turbo"
    GPT4 = "GPT4"
    GPT4O = "GPT4O"
    GPT4OMini = "GPT4OMini"


class PromptStyle(Enum):
    Full = "Full"
    Summarized = "Summarized"


@dataclass
class PromptContentParams:
    location: str
    account_id: str
    video_id: str
    model_name: Optional[ModelName] = None
    prompt_style: Optional[PromptStyle] = None


class VideoIndexerService:
    BASE_URL = "https://api.videoindexer.ai"

    def __init__(self, access_token: str):
        if not access_token:
            raise ValueError("Access token is required")
        self.access_token = access_token

    def _get_headers(self):
        return {
            "Content-Type": "application/json"
        }

    def _validate_params(self, params: PromptContentParams) -> None:
        """Validate common parameters"""
        if not params.location:
            raise ValueError("Location is required")
        if not params.account_id:
            raise ValueError("Account ID is required")
        if not params.video_id:
            raise ValueError("Video ID is required")

    def _make_request(self, method: HttpMethod, url: str, query_params: Dict[str, Any]) -> Any:
        """Make HTTP request with error handling"""
        try:
            with httpx.Client() as client:
                response = getattr(client, method.lower())(
                    url,
                    headers=self._get_headers(),
                    params=query_params
                )
                response.raise_for_status()
                return response.json() if method == "GET" else f"{response.status_code}: Prompt content job started - {response.text}"
        except httpx.HTTPStatusError as e:
            error_messages = {
                400: "Bad request",
                401: "Unauthorized",
                404: "not found",
                409: "conflict"
            }
            if e.response.status_code in error_messages:
                raise ValueError(
                    f"{error_messages[e.response.status_code]} - {e.response.text}")
            raise

    def create_prompt_content(self, params: PromptContentParams) -> str:
        """Create prompt content for a video"""
        self._validate_params(params)

        url = f"{self.BASE_URL}/{params.location}/Accounts/{params.account_id}/Videos/{params.video_id}/PromptContent"
        query_params = {"accessToken": self.access_token}

        if params.model_name:
            query_params["modelName"] = params.model_name.value
        if params.prompt_style:
            query_params["promptStyle"] = params.prompt_style.value

        return self._make_request("POST", url, query_params)

    def get_prompt_content(self, params: PromptContentParams) -> Dict[str, Any]:
        """Get prompt content for a video"""
        self._validate_params(params)

        url = f"{self.BASE_URL}/{params.location}/Accounts/{params.account_id}/Videos/{params.video_id}/PromptContent"
        query_params = {"accessToken": self.access_token}

        return self._make_request("GET", url, query_params)
