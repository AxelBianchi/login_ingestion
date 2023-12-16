import datetime
from datetime import datetime

def verif_msg(message_json):

    client_id = message_json.get('client_id')
    login_timestamp = message_json.get('login_timestamp')

    #Vérifier l'existence du client_id
    if client_id is None:
        error_message = "Invalid client_id"
        return error_message

    #Vérifier la cohérence du login_timestamp
    current_time = datetime.utcnow().timestamp()
    max_acceptable_timestamp = current_time + 3600  #Marge d'une heure pour éviter les problèmes de synchronisation
    if login_timestamp > max_acceptable_timestamp or login_timestamp < 0:
        error_message = "Invalid Timestamp"
        return error_message

    else:
        error_message = None
        return error_message