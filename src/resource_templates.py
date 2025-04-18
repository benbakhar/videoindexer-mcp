import re
from typing import Dict, Any, List
from urllib.parse import unquote
from modelcontextprotocol_sdk.server import Server
from modelcontextprotocol_sdk.types import (
    ListResourceTemplatesRequestSchema,
    ReadResourceRequestSchema,
)

RESOURCE_TEMPLATES = [
    {
        "uriTemplate": "videos://search/{query}",
        "name": "Video Search",
        "description": "Search videos by query",
        "mimeType": "text/plain",
    },
    {
        "uriTemplate": "videos://promptContent/{videoId}",
        "name": "Video Prompt Content",
        "description": "Get prompt content for a video",
        "mimeType": "text/plain",
    },
]

def setup_resource_template_handlers(server: Server) -> None:
    @server.request_handler(ListResourceTemplatesRequestSchema)
    async def list_resource_templates():
        return {"resourceTemplates": RESOURCE_TEMPLATES}

    @server.request_handler(ReadResourceRequestSchema)
    async def read_resource(request: Dict[str, Any]):
        uri = request["params"]["uri"]

        # Check for prompt content template match
        prompt_content_pattern = r"^videos://promptContent/(.+)$"
        if match := re.match(prompt_content_pattern, uri):
            video_id = match.group(1)
            return {
                "contents": [
                    {
                        "uri": uri,
                        "text": f"Prompt content for video ID - {video_id}! Welcome to video indexer MCP.",
                    }
                ]
            }

        # Check for video search template match
        search_pattern = r"^videos://search/(.+)$"
        if match := re.match(search_pattern, uri):
            query = unquote(match.group(1))
            return {
                "contents": [
                    {
                        "uri": uri,
                        "text": f"query to apply - {query}! Welcome to video indexer MCP.",
                    }
                ]
            }

        # Return empty contents if no matches
        return {"contents": []}
