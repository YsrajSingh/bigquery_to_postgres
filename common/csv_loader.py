import pandas as pd


# Load data from CSV file into Pandas DataFrame
def csv_connection(FilePath, chunk_size):
    return pd.read_csv(FilePath, chunksize=chunk_size)


def get_csv(FilePath, FileName, chunk_size):
    try:
        # GET THE REQUIRED CSV FILE and SHOW DATA OF FILE
        chunk = csv_connection(FilePath, chunk_size)
        print(f"CSV File : {FileName} Data Loaded Successfully")
        return chunk

    except Exception as ex:
        print("CSV File is not loaded Successfully: \n", ex)
        return None
