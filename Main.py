import base64

def ingest_message(event, context):
    message = base64.b64decode(event['data']).decode('utf-8') #Récup event sans le reste (event et context)
    print(message)


