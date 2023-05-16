from settings.settings import NEW_DATABASE_URL, TABLE_NAME, CSV_FILE
from .db_connection import get_database
from .csv_loader import get_csv

engine = get_database(NEW_DATABASE_URL)
csv_file = get_csv(CSV_FILE)

if engine is None:
    raise Exception("Could not connect to the database")

if csv_file is None:
    raise Exception("Could not load the CSV file")
