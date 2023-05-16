from . import engine, csv_file
import pandas as pd
from settings.settings import TABLE_NAME, JSON_FILE_PATH
import json
from sqlalchemy import inspect


# Load JSON file containing column mapping
with open(JSON_FILE_PATH) as f:
    column_mapping = json.load(f)

# Get the columns of the existing table
inspector = inspect(engine)

if TABLE_NAME not in inspector.get_table_names():
    raise Exception("Table does not exist")

existing_columns = [column["name"] for column in inspector.get_columns(TABLE_NAME)]


def script():
    # Verify CSV column existence and migrate data to database
    csv_columns = list(csv_file.columns)
    db_columns = [mapping["destination_column"] for mapping in column_mapping]

    if not all(column in csv_columns for column in db_columns):
        missing_columns = set(db_columns) - set(csv_columns)
        print(f"CSV columns {missing_columns} not found.")
    else:
        try:
            # Create a DataFrame with selected columns from the CSV file
            data_frame = csv_file[
                [mapping["source_column"] for mapping in column_mapping]
            ]

            # Rename the columns based on the mapping
            data_frame.rename(
                columns={
                    mapping["source_column"]: mapping["destination_column"]
                    for mapping in column_mapping
                },
                inplace=True,
            )

            # Append the data to the existing table
            data_frame.to_sql(TABLE_NAME, engine, if_exists="append", index=False)

            print("Data migrated successfully.")
        except Exception as ex:
            print("There was an error migrating data:")
            print(ex)

    # Close connection
    engine.dispose()
