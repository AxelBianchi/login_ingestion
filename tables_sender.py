from google.cloud import bigquery

def message_to_login(message_json_format):
    print("GOOD MESSAGE")

    client = bigquery.Client()

    project_id = "ethereal-casing-404517"
    dataset_id = "ethereal-casing-404517.raw_dataset"
    table_id = "ethereal-casing-404517.raw_dataset.login"

    # Insert data into BigQuery
    rows_to_insert = [message_json_format]

    errors = client.insert_rows_json(table_id, rows_to_insert)

    if errors == []:
        print("Data inserted successfully")
    else:
        print("Errors encountered:", errors)

