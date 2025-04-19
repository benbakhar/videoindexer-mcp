from setuptools import setup, find_packages

setup(
    name="videoindexer-mcp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "modelcontextprotocol-sdk",
        "pydantic",
        "python-dotenv",
        "httpx",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "videoindexer-mcp=src.server:main",
        ],
    },
    author="Ben Bakhar",
    description="Video Indexer MCP Server",
    keywords="mcp, azure ai video indexer, server",
)
