import base64
import json
from messageProcessing import verif_msg,get_error_reason
from tables_sender import message_to_login, message_to_login_error

def ingest_message(event, context):
    message = base64.b64decode(event['data']).decode('utf-8') #Récup event sans le reste (event et context)
    print(message)

    message_json = json.loads(message)
    error_code = verif_msg(message_json)

    if error_code == 0:
        message_to_login(message_json)

    else:
        message_reason = get_error_reason(error_code)
        message_to_login_error(message_json,message_reason)


