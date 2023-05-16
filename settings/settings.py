import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# import requirements
NEW_DATABASE_URL = os.environ.get("DATABASE_URL")
TABLE_NAME = os.environ.get("TABLE_NAME")
CSV_FILE = os.environ.get("CSV_FILE")
JSON_FILE_PATH = os.environ.get("JSON_FILE_DATA")
