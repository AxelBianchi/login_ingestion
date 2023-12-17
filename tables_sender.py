from google.cloud import bigquery
import json

def message_to_login(message_json_format):
    print("GOOD MESSAGE")

    client = bigquery.Client()
    table_id = "ethereal-casing-404517.raw_dataset.login"

    # Insert data into BigQuery
    rows_to_insert = [message_json_format]

    errors = client.insert_rows_json(table_id, rows_to_insert)

    if errors == []:
        print("Data inserted successfully")
    else:
        print("Errors encountered:", errors)

def message_to_login_error(message_json_format,reason):
    print("BAD MESSAGE")

    client = bigquery.Client()
    table_id = "ethereal-casing-404517.raw_dataset.login"

    # Construction de l'objet d'insertion avec les champs spécifiés
    rows_to_insert = [{
        'client_id': message_json_format['client_id'],
        'login_timestamp': message_json_format['login_timestamp'],
        'device_type': message_json_format['device_type'],
        'browser': message_json_format['browser'],
        'os': message_json_format['os'],
        'reason': reason
    }]

    errors = client.insert_rows_json(table_id, rows_to_insert)

    if errors == []:
        print("Data inserted successfully")
    else:
        print("Errors encountered:", errors)
