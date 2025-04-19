from mcp.server.fastmcp import FastMCP

# @NOTE: workaround to a bug with cline. log level must be set to ERROR
mcp = FastMCP("Video Indexer MCP", log_level="ERROR")
