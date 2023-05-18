# Migration Script

This repository contains a migration script designed to facilitate the transfer of data from BigQuery to a Postgres database.

## Getting Started

To run this project, please follow the steps outlined below:

- Clone the repository and navigate to the project directory.

- Create and activate a virtual environment by executing the following commands:

```bash
python -m venv .venv

source .venv/bin/activate
```

- Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

- Customize the environment variables:

  Refer to the provided .env.example file for an example. Create a .env file and set the following environment variables:

```bash
DATABASE_URL=<your-database-url>

CSV_CHUNK_SIZE=<chunk-size>

```

Replace <your-database-url> with the URL of your Postgres database and <chunk-size> with an appropriate integer value.

- Update the migration configuration:

  Open the migration.json file and modify the values for BigQueryTable, PostgresTable, source_column, and destination_column based on your specific requirements. Ensure that the CSV file specified in BigQueryTable exists in the static folder, and that both source_column and destination_column are valid column names in their respective tables.

- Run the migration script:

```bash
python index.py
```

The script will retrieve data from BigQuery according to the specified configuration and migrate it to the Postgres database.

## Notes

- Make sure to install the required dependencies listed in the requirements.txt file.

- This script assumes that you have a Postgres database set up and accessible via the provided DATABASE_URL environment variable.

- Ensure that the necessary permissions and access rights are set up for both the BigQuery and Postgres databases.

- Take into account the size of the data being migrated and the performance implications of inserting data row by row. Consider using bulk insertion methods for better performance if applicable.

- It is recommended to review and understand the code in the script before running it to ensure it meets your specific requirements and data migration needs.
