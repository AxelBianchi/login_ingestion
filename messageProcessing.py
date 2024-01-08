import datetime
from datetime import datetime

error_codes = {
    "invalid_client_id": 1,
    "invalid_timestamp": 2,
    "valid_login_message": 0
}

def verify_message(message_json):

    client_id = message_json.get('client_id')
    if client_id is None:
        return error_codes["invalid_client_id"]

    login_timestamp = message_json.get('login_timestamp')
    current_time = datetime.utcnow().timestamp()
    if login_timestamp > current_time:
        return error_codes["invalid_timestamp"]

    else:
        return error_codes["valid_login_message"]