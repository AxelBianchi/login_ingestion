import base64
import json
from messageProcessing import verif_msg
from tables_sender import message_to_login

codes = {
    1: "error_client_id",
    2: "error_timestamp",
    3: "normal_login"
}

def ingest_message(event, context):
    message = base64.b64decode(event['data']).decode('utf-8') #Récup event sans le reste (event et context)
    print(message)

    message_json = json.load(event['data'])
    error_code = verif_msg(message_json)
    error_message = codes[error_code]

    if error_code == 3:
        message_to_login(message_json)
