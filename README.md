# Video Indexer MCP Server

A Python implementation of the Video Indexer MCP server that provides tools and resources for interacting with Video Indexer APIs.

## Features

- Tools:
  - `upload_video`: Upload a video to Video Indexer with specified preset

- Resource Templates:
  - Video search functionality
  - Video prompt content retrieval

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

## Configuration

Add your VI account token to `cline_mcp_settings.json`:

## Usage

Start the server:
```bash
python -m src./main.py
```

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
