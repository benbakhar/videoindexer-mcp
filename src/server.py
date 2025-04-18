import os
import asyncio
from dotenv import load_dotenv
from modelcontextprotocol_sdk.server import Server

from tools import setup_tool_handlers
from resources import setup_resource_handlers
from resource_templates import setup_resource_template_handlers

def create_server() -> Server:
    """Create and configure the MCP server."""
    server = Server()
    
    # Set up all handlers
    setup_tool_handlers(server)
    setup_resource_handlers(server)
    setup_resource_template_handlers(server)
    
    return server

async def main() -> None:
    """Main entry point for the server."""
    # Load environment variables
    load_dotenv()
    
    # Create and start server
    server = create_server()
    await server.start()

if __name__ == "__main__":
    # Run the server
    asyncio.run(main())
