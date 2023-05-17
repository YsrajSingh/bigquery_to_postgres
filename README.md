# Migration Script

This is a migration script that allows you to migrate data from BigQuery to a Postgres database.

## Getting Started

To run this project, you need to follow these steps:

- Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
```

- Navigate to the project directory:

```bash
cd your-repo
```

- Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

- Install the required dependencies:

```bash
pip install -r requirements.txt
```

- Customize the environment variables:

  Create a .env file and set the following environment variable:

```bash
DATABASE_URL=<your-database-url>
```

Replace <your-database-url> with the URL of your Postgres database.

- Update the migration configuration:

  In the migration.json file, update the values for BigQueryTable, PostgresTable, source_column, and destination_column according to your requirements. Ensure that the CSV file specified in BigQueryTable exists in the static folder, and that both source_column and destination_column are valid column names in their respective tables.

- Run the migration script:

```bash
python index.py
```

The script will fetch data from BigQuery based on the specified configuration and migrate it to the Postgres database.

## Notes

- Make sure to install the required dependencies listed in the requirements.txt file.

- This script assumes that you have a Postgres database set up and accessible via the provided DATABASE_URL environment variable.

- Ensure that the necessary permissions and access rights are set up for both the BigQuery and Postgres databases.

- Take into account the size of the data being migrated and the performance implications of inserting data row by row. Consider using bulk insertion methods for better performance if applicable.

- It is recommended to review and understand the code in the script before running it to ensure it meets your specific requirements and data migration needs.

## License

- This project is licensed under the MIT License.
