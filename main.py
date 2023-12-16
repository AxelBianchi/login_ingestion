import base64
import json
from verif_msg import verif_msg
from message_to_login import message_to_login
from message_to_login_error import message_to_login_error

def ingest_message(event):
    message = base64.b64decode(event['data']).decode('utf-8') #Récup event sans le reste (event et context)
    print(message)

    message_json = json.load(event['data'].decode('utf-8'))
    error_message = verif_msg(message_json)
    if error_message is None:
        print("fonction normale")
        message_to_login(message_json) #Ecrire dans la table normale
    if error_message is not None:
        print("non")
        message_to_login_error(message_json)
