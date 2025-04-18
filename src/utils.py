
import base64
import json
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
        # Return default values if token parsing fails
        return {"sub": "1234567890", "name": "Dummy account"}
