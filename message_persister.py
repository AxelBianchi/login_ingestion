import os

from google.cloud import bigquery

def persist_message(message, error_code):
    client = bigquery.Client()

    destination_table = os.getenv("LOGIN_TABLE_NAME") if error_code == 0 else os.getenv("LOGIN_ERROR_TABLE_NAME")
    table_id = os.getenv("PROJECT_ID") + "." + os.getenv("DATASET_NAME") + "." +  destination_table

    rows_to_insert = [message]

    errors = client.insert_rows_json(table_id, rows_to_insert)

    if errors == []:
        print("Data inserted successfully in table: " + destination_table)
    else:
        print("Errors encountered:", errors)