## Video Indexer MCP Server
A Model Context Protocol (MCP) server that provides tools and resources for interacting with Video Indexer APIs.

### Features

- `vi_prompt_content`: Generate prompt content from video insights
- `vi_get_prompt_content`: Get the generated prompt content for a video

### Use Cases

- feed LLMs with video insights
- Automated API interactions

### example config

```json
{
  "mcpServers": {
    "videoindexer-mcp": {
      "command": "/path/to/videoindexer-mcp/bin/python",
      "args": [
        "/path/to/your/videoindexer-mcp/src/main.py",
      ],
      "env": {
        "VI_ACCOUNT_TOKEN": "<your_video_indexer_account_token>",
      },
      "transportType": "stdio"
    }
  }
}
```

Replace `/path/to/videoindexer-mcp` with the actual path to your videoindexer-mcp directory.

## Installation

1. Clone the repository
2. Create and activate a Python virtual environment:
```bash
# Create virtual environment
python -m venv mcp-env

# Activate virtual environment
# On Windows:
mcp-env\Scripts\activate
# On Unix or MacOS:
source mcp-env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Install the package:
```bash
pip install -e .
```

5. To deactivate the virtual environment when you're done:
```bash
deactivate
```