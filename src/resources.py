import os
from typing import Dict
from server import mcp
from utils import extract_jwt

token = os.getenv("VI_ACCOUNT_TOKEN")
if not token:
    raise ValueError("VI_ACCOUNT_TOKEN environment variable is not set")


@mcp.resource("account://name")
def account_resource() -> Dict[str, str]:
    """returns the account resource"""

    # Extract JWT from env variable
    name = extract_jwt(token).get("name", "Fallback account name")

    return {
        "uri": "account://name",
        "name": name,
        "description": "your vi account name",
        "mimeType": "text/plain",
    }
