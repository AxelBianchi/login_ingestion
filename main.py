import base64
import json
from messageProcessing import verify_message,get_error_reason
from message_persister import message_to_login, message_to_login_error, persist_message


def ingest_message(event, context):
    message = base64.b64decode(event['data']).decode('utf-8') #Récup event sans le reste (event et context)
    print(message)
    message_json = json.loads(message)
    error_code = verify_message(message_json)

    if error_code == 0:
        persist_message(message_json, error_code)

    else:
        message_json["reason"] = "invalid_client_id" if error_code == 1 else "invalid_timestamp"
        persist_message(message_json, error_code)


