from server import mcp

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


@mcp.tool()
def upload_video(url: str, preset: str) -> str:
    """upload a video to your videoindexer (vi) account"""
    return f"upload video: {url} with preset: {preset}"


print("Tools loaded successfully")
