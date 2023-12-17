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
    print("BAD MESSAGE ")
    message_json_str = str(message_json_format).replace("'", '"')
    message_json = json.loads(message_json_str)

    client = bigquery.Client()
    table_id = "ethereal-casing-404517.raw_dataset.login_errors"

    message_json["reason"] = reason
    print(message_json)
    # Insert data into BigQuery
    rows_to_insert = [message_json]

    errors = client.insert_rows_json(table_id, rows_to_insert)

    if errors == []:
        print("Data inserted successfully")
    else:
        print("Errors encountered:", errors)

