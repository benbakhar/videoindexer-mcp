
import base64
import json
import os
from typing import Dict


def extract_jwt(token: str) -> Dict[str, str]:
    """Extract and decode JWT payload."""
    try:
        if not token:
            raise ValueError("No token provided")

        parts = token.split(".")
        if len(parts) != 3:
            raise ValueError("Invalid JWT format")

        payload = parts[1]
        # Add padding if needed
        padding = len(payload) % 4
        if padding:
            payload += "=" * (4 - padding)

        decoded_payload = base64.urlsafe_b64decode(payload).decode("utf-8")
        return json.loads(decoded_payload)
    except Exception as e:
        raise ValueError(f"Failed to parse JWT token: {str(e)}")


def get_access_token() -> str:
    """Get the access token from the environment variable."""
    token = os.getenv("VI_ACCOUNT_TOKEN")

    if not token:
        raise ValueError(
            "VI_ACCOUNT_TOKEN environment variable is not set. Please set the VI_ACCOUNT_TOKEN environment variable to your Video Indexer account token.")

    return token
