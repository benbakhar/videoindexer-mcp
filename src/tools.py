from server import mcp
from services.videoindexer import VideoIndexerService, ModelName, PromptStyle, PromptContentParams
from utils import get_access_token

tools = [
    {
        "name": "vi_create_prompt_content",
        "description": "Generate Prompt Content from video insights",
        "inputSchema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Azure region to which the call should be routed"
                },
                "accountId": {
                    "type": "string",
                    "description": "Account ID (GUID) for the account"
                },
                "videoId": {
                    "type": "string",
                    "description": "The video ID"
                },
                "modelName": {
                    "type": "string",
                    "description": "The LLM tokenizer to create the prompt content",
                    "enum": ["Llama2", "Phi2", "Phi3", "Phi3_5", "GPT3_5Turbo", "GPT4", "GPT4O", "GPT4OMini"]
                },
                "promptStyle": {
                    "type": "string",
                    "description": "Style of the prompt",
                    "enum": ["Full", "Summarized"]
                }
            },
            "required": ["location", "accountId", "videoId"]
        },
    },
    {
        "name": "vi_get_prompt_content",
        "description": "Get the generated prompt content for a video",
        "inputSchema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Azure region to which the call should be routed"
                },
                "accountId": {
                    "type": "string",
                    "description": "Account ID (GUID) for the account"
                },
                "videoId": {
                    "type": "string",
                    "description": "The video ID"
                }
            },
            "required": ["location", "accountId", "videoId"]
        },
    },
]


@mcp.tool()
def vi_create_prompt_content(location: str, accountId: str, videoId: str, modelName: str = None, promptStyle: str = None) -> str:
    """Generate Prompt Content from video insights"""

    if not location:
        raise ValueError("Location is required")
    if not accountId:
        raise ValueError("Account ID is required")
    if not videoId:
        raise ValueError("Video ID is required")

    try:
        access_token = get_access_token()
        service = VideoIndexerService(access_token)

        model = None
        if modelName is not None:
            try:
                model = ModelName[modelName]
            except KeyError:
                raise ValueError(
                    f"Invalid model name. Must be one of: {', '.join(ModelName.__members__.keys())}"
                )

        style = None
        if promptStyle is not None:
            try:
                style = PromptStyle[promptStyle]
            except KeyError:
                raise ValueError(
                    f"Invalid prompt style. Must be one of: {', '.join(PromptStyle.__members__.keys())}"
                )

        params = PromptContentParams(
            location=location,
            account_id=accountId,
            video_id=videoId,
            model_name=model,
            prompt_style=style
        )

        return service.create_prompt_content(params)

    except Exception as e:
        raise ValueError(str(e))


@mcp.tool()
def vi_get_prompt_content(location: str, accountId: str, videoId: str) -> dict:
    """Get the generated prompt content for a video"""

    if not location:
        raise ValueError("Location is required")
    if not accountId:
        raise ValueError("Account ID is required")
    if not videoId:
        raise ValueError("Video ID is required")

    try:
        access_token = get_access_token()
        service = VideoIndexerService(access_token)

        params = PromptContentParams(
            location=location,
            account_id=accountId,
            video_id=videoId
        )

        return service.get_prompt_content(params)

    except Exception as e:
        raise ValueError(str(e))
