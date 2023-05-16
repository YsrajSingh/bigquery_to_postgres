
# Migration Script

Migrate data from BigQuery to Postgres Database


## Environment Variables

To run this project, you will need to customize the following environment variables to your .env file

`DATABASE_URL`

`TABLE_NAME`

`CSV_FILE`


## Customizations

We have to specify source and destination columns in
```bash
migration.json
```
file.


## Run Locally

Create Virtual Environment

```bash
  python -m env .venv
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the Script

```bash
  python index.py
```

