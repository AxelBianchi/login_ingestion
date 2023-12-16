from google.cloud import bigquery

def message_to_login(message_json_format):
    print("GOOD MESSAGE")

    client = bigquery.Client()

    project_id = "ethereal-casing-404517"
    dataset_id = "ethereal-casing-404517.raw_dataset"
    table_id = "ethereal-casing-404517.raw_dataset.login"

    table_ref = client.get_table(f"{project_id}.{dataset_id}.{table_id}")

    # Insert data into BigQuery
    rows_to_insert = [(
        message_json_format['client_id'],
        message_json_format['login_timestamp'],
        message_json_format['device_type'],
        message_json_format['browser'],
        message_json_format['os']
    )]

    errors = client.insert_rows(table_ref, rows_to_insert)
    if errors == []:
        print("Data inserted successfully")
    else:
        print("Errors encountered: ", errors)

