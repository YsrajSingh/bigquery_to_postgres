from settings.settings import NEW_DATABASE_URL, CSV_FILE, JSON_FILE_PATH, CSV_CHUNK_SIZE
from .db_connection import get_database
from .csv_loader import get_csv
import json

engine = get_database(NEW_DATABASE_URL)
if engine is None:
    raise Exception("Could not connect to the database.")

# Load JSON file containing column mapping
with open(JSON_FILE_PATH) as f:
    json_data = json.load(f)


def csv_data(BigQueryTableName, CSV_CHUNK_SIZE=CSV_CHUNK_SIZE):
    TablePath = CSV_FILE + BigQueryTableName
    csv_file = get_csv(TablePath, BigQueryTableName, CSV_CHUNK_SIZE)

    if csv_file is None:
        raise Exception("Could not load the CSV file of BigQuery.")

    return csv_file
