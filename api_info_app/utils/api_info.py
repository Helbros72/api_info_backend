import requests

from api_info_app.utils.safe_to_history import safe_to_history

URL = "http://ip-api.com/json/"


def get_api_info(api_address):
    try:
        response = requests.get(f"{URL}{api_address}")
        json_response = response.json()
    except Exception as e:
        return {"error": str(e)}
    return json_response


