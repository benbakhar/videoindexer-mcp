from typing import Dict, Any
from modelcontextprotocol_sdk.server import Server
from modelcontextprotocol_sdk.types import (
    CallToolRequestSchema,
    ListToolsRequestSchema,
    McpError,
    ErrorCode,
)

tools = [
    {
        "name": "create_note",
        "description": "Create a new note",
        "inputSchema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title of the note",
                },
                "content": {
                    "type": "string",
                    "description": "Text content of the note",
                },
            },
            "required": ["title", "content"],
        },
    },
    {
        "name": "upload_video",
        "description": "Upload a video to VI account",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "url of the video to upload",
                },
                "preset": {
                    "type": "string",
                    "description": "Preset to use for the video upload",
                },
            },
            "required": ["url", "preset"],
        },
    },
]

async def handle_create_note(arguments: Dict[str, Any]) -> Dict[str, Any]:
    title = arguments.get("title")
    content = arguments.get("content")
    note_id = {"title": title, "content": content}
    
    return {
        "content": [
            {
                "type": "text",
                "text": f"Note created with ID {note_id}",
            }
        ]
    }

def setup_tool_handlers(server: Server) -> None:
    # List available tools
    @server.request_handler(ListToolsRequestSchema)
    async def list_tools():
        return {"tools": tools}

    # Handle tool calls
    @server.request_handler(CallToolRequestSchema)
    async def call_tool(request: Dict[str, Any]):
        tool_name = request["params"]["name"]
        arguments = request["params"].get("arguments")

        if tool_name not in [tool["name"] for tool in tools]:
            raise McpError(
                ErrorCode.MethodNotFound,
                f"Unknown tool: {tool_name}"
            )

        if not arguments:
            raise McpError(
                ErrorCode.InvalidRequest,
                "Arguments are required"
            )

        if tool_name == "create_note":
            return await handle_create_note(arguments)
        
        raise McpError(
            ErrorCode.MethodNotFound,
            f"Handler not implemented for tool: {tool_name}"
        )
