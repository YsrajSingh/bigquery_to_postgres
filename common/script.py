from . import engine, csv_data, json_data
from settings.settings import JSON_FILE_PATH
from .config import (
    BIGQUERY_TABLE,
    POSTGRES_TABLE,
    SOURCE_COLUMN,
    DESTINATION_COLUMNS,
    ALL_COLUMNS,
)
from sqlalchemy import inspect


# Get the columns of the existing table
inspector = inspect(engine)


def script():
    for data in json_data:
        print(f"=====================MIGRATION INITIATED======================\n")

        TABLE_NAME = data[POSTGRES_TABLE]
        bigQuery_Table = data[BIGQUERY_TABLE]
        csv_file = csv_data(bigQuery_Table)
        column_mapping = data[ALL_COLUMNS]

        if TABLE_NAME not in inspector.get_table_names():
            raise Exception("Table does not exist")

        try:
            # Create a copy of the DataFrame with selected columns from the CSV file
            selected_columns = [mapping[SOURCE_COLUMN] for mapping in column_mapping]
            data_frame = csv_file.loc[:, selected_columns].copy()

            # Rename the columns based on the mapping
            column_mapping_dict = {
                mapping[SOURCE_COLUMN]: mapping[DESTINATION_COLUMNS]
                for mapping in column_mapping
            }
            data_frame.rename(columns=column_mapping_dict, inplace=True)

            # Append the data to the existing table
            data_frame.to_sql(TABLE_NAME, engine, if_exists="append", index=False)

            print(f"{bigQuery_Table} Data migrated to {TABLE_NAME} successfully.\n")
            print(f"=====================MIGRATION COMPLETED======================\n")

        except Exception as ex:
            print("There was an error migrating data.\n")
            print(ex)

    # Close connection
    engine.dispose()
