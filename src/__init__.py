"""
Video Indexer MCP Server
~~~~~~~~~~~~~~~~~~~~~~~

A Python implementation of the Video Indexer MCP server that provides
tools and resources for interacting with Video Indexer services.
"""

from .server import create_server, main
from .tools import setup_tool_handlers
from .resources import setup_resource_handlers
from .resource_templates import setup_resource_template_handlers

__version__ = "0.1.0"
__all__ = [
    "create_server",
    "main",
    "setup_tool_handlers",
    "setup_resource_handlers",
    "setup_resource_template_handlers",
]
