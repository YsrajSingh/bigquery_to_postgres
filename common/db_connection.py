from sqlalchemy import create_engine


# Set up PostgreSQL connection
def db_connection(DB_url):
    return create_engine(url=DB_url)


def get_database(DB_url):
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = db_connection(DB_url)
        print(f"Connection to the {engine} created successfully.")
        return engine

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
        return None
