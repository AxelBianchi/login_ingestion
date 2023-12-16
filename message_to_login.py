from google.cloud import bigquery

def message_to_login(message_json_format):
    print("GOOD MESSAGE")

    client = bigquery.Client()

    project_id = "ethereal-casing-404517"
    dataset_id = "ethereal-casing-404517.raw_dataset"
    table_id = "ethereal-casing-404517.raw_dataset.login"

    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    rows_to_insert = [(message_json_format['client_id'], ......)]

    errors = client.insert_rows(table, rows_to_insert)