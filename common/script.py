from . import engine, csv_data, json_data
from sqlalchemy import inspect, MetaData, Table
from settings.settings import CSV_CHUNK_SIZE
from .config import (
    BIGQUERY_TABLE,
    POSTGRES_TABLE,
    SOURCE_COLUMN,
    DESTINATION_COLUMNS,
    ALL_COLUMNS,
)

# Get the columns of the existing table
inspector = inspect(engine)

metadata = MetaData()
# Associate the engine with the metadata object
metadata.reflect(bind=engine)


def script():
    for data in json_data:
        print(f"=====================MIGRATION INITIATED======================\n")

        total_rows = 0
        table_name = data[POSTGRES_TABLE]
        bigQuery_Table = data[BIGQUERY_TABLE]
        csv_file = csv_data(bigQuery_Table)
        column_mapping = data[ALL_COLUMNS]

        if table_name not in inspector.get_table_names():
            raise Exception("Table does not exist")

        # Create the SQLAlchemy table object for the destination table
        table = metadata.tables[table_name]

        try:
            # Create a copy of the DataFrame with selected columns from the CSV file
            selected_columns = [mapping[SOURCE_COLUMN] for mapping in column_mapping]

            for index, chunk in enumerate(csv_file):
                start_row = index * CSV_CHUNK_SIZE + 1  # Calculate starting row number
                end_row = start_row + len(chunk) - 1  # Calculate ending row number
                modified_data = []
                modified_row = {}
                for _, row in chunk.iterrows():
                    modified_row = {}
                    for column in selected_columns:
                        # Apply any necessary modifications to the column values
                        modified_value = row[column]

                        # Rename the column based on the mapping
                        for mapping in column_mapping:
                            if mapping[SOURCE_COLUMN] == column:
                                modified_column = mapping[DESTINATION_COLUMNS]
                                break
                        else:
                            modified_column = column

                        modified_row[modified_column] = modified_value

                    modified_data.append(modified_row)
                # Perform operations on each chunk of data
                # For example, you can process or analyze the chunk here
                print(f"{start_row} to {end_row} rows loaded successfully.")

                total_rows += len(row)  # Update the total rows counter

                # Append the modified data to the existing table

                with engine.begin() as connection:
                    for index, row in enumerate(modified_data):
                        # Generate the SQLAlchemy insert statement
                        insert_stmt = table.insert().values(**row)

                        # Execute the insert statement
                        connection.execute(insert_stmt)

                print(f"{start_row} to {end_row} are migrated to database.")
                print(f"==================================================")

            print(f"{bigQuery_Table} Data migrated to {table_name} successfully.\n")
            print(f"=====================MIGRATION COMPLETED======================\n")

        except Exception as ex:
            print("There was an error migrating data.\n")
            print(ex)

    # Close connection
    engine.dispose()
