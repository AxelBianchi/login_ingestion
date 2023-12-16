import base64
import json
from messageProcessing import verif_msg
from tables_sender import message_to_login

error_codes = {
    "error_client_id": 0,
    "error_timestamp": 1,
    "normal_login": 2
}

def ingest_message(event, context):
    message = base64.b64decode(event['data']) #Récup event sans le reste (event et context)
    print(message)

    message_json = json.loads(event['data'])
    error_code = verif_msg(message_json)
    error_message = codes[error_code]

    if error_code == 3:
        message_to_login(message_json)
