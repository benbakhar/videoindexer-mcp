import os
import base64
import json
from typing import Dict
from modelcontextprotocol_sdk.server import Server
from modelcontextprotocol_sdk.types import ListResourcesRequestSchema

def extract_jwt(token: str) -> Dict[str, str]:
    """Extract and decode JWT payload."""
    try:
        payload = token.split(".")[1]
        # Add padding if needed
        padding = len(payload) % 4
        if padding:
            payload += "=" * (4 - padding)
        
        decoded_payload = base64.b64decode(payload).decode("utf-8")
        return json.loads(decoded_payload)
    except (IndexError, json.JSONDecodeError) as e:
        # Return default values if token parsing fails
        return {"sub": "1234567890", "name": "John Doe"}

def setup_resource_handlers(server: Server) -> None:
    # Default JWT token for testing
    default_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"
    
    # Extract token from environment or use default
    token = os.environ.get("VI_ACCOUNT_TOKEN", default_token)
    jwt_data = extract_jwt(token)

    @server.request_handler(ListResourcesRequestSchema)
    async def list_resources():
        return {
            "resources": [
                {
                    "uri": f"account:///{jwt_data['sub']}",
                    "name": jwt_data['name'],
                    "description": "your vi account",
                    "mimeType": "text/plain",
                }
            ]
        }
