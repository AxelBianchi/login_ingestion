import base64
import json
from messageProcessing import verif_msg, error_codes
from tables_sender import message_to_login

def ingest_message(event, context):
    message = base64.b64decode(event['data']) #Récup event sans le reste (event et context)
    print(message)

    message_json = json.loads(message)
    error_code = verif_msg(message_json)

    if error_code == 0:
        message_to_login(message_json)
