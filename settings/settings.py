import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# import requirements
NEW_DATABASE_URL = os.environ.get("DATABASE_URL")
CSV_FILE = os.environ.get("CSV_FILE")
JSON_FILE_PATH = os.environ.get("JSON_FILE_DATA")
CSV_CHUNK_SIZE = os.environ.get("CSV_CHUNK_SIZE")

# Chunk Size must be integer every time
CSV_CHUNK_SIZE = int(CSV_CHUNK_SIZE)
