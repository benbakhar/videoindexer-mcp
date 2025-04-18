# Video Indexer MCP Server

A Python implementation of the Video Indexer MCP server that provides tools and resources for interacting with Video Indexer services.

## Features

- Tools:
  - `create_note`: Create a new note with title and content
  - `upload_video`: Upload a video to Video Indexer with specified preset

- Resources:
  - Account information with JWT-based authentication

- Resource Templates:
  - Video search functionality
  - Video prompt content retrieval

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install the package:
```bash
pip install -e .
```

## Configuration

Create a `.env` file in the project root with the following variables:
```
VI_ACCOUNT_TOKEN=your_jwt_token_here
```

## Usage

Start the server:
```bash
python -m src.server
```

The server will start and listen for MCP requests, providing:
- Tool endpoints for note creation and video uploads
- Resource endpoints for account information
- Resource template endpoints for video search and prompt content

## Development

The project structure:
```
videoindexer-mcp/
├── requirements.txt    # Project dependencies
├── setup.py           # Package installation configuration
├── README.md          # Project documentation
└── src/              
    ├── __init__.py
    ├── server.py      # Main server implementation
    ├── tools.py       # Tool definitions and handlers
    ├── resources.py   # Resource handlers
    └── resource_templates.py  # Resource template handlers
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
