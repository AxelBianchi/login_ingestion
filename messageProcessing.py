import datetime
from datetime import datetime

error_codes = {
    "error_client_id": 0,
    "error_timestamp": 1,
    "normal_login": 2
}

def verif_msg(message_json):

    client_id = message_json.get('client_id')
    login_timestamp = message_json.get('login_timestamp')

    #Vérifier l'existence du client_id
    if client_id is None:
        return error_codes["error_client_id"]

    #Vérifier la cohérence du login_timestamp
    current_time = datetime.utcnow().timestamp()
    if login_timestamp > current_time:
        return error_codes["error_timestamp"]

    else:
        return error_codes["normal_login"]