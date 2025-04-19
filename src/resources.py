from typing import Dict
from server import mcp
from utils import extract_jwt, get_access_token


@mcp.resource("account://id")
def account_resource() -> Dict[str, str]:
    """returns the account id"""

    try:
        token = get_access_token()
        payload = extract_jwt(token)
        name = payload["AccountId"]
    except Exception as e:
        raise ValueError(f"Failed to get account id: {str(e)}")

    return {
        "uri": "account://name",
        "name": name,
        "description": "your vi account name",
        "mimeType": "text/plain",
    }
