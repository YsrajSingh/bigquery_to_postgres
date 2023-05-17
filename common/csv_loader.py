import pandas as pd


# Load data from CSV file into Pandas DataFrame
def csv_connection(FilePath):
    return pd.read_csv(FilePath)


def get_csv(FilePath, FileName):
    try:
        # GET THE REQUIRED CSV FILE and SHOW DATA OF FILE
        csv_file = csv_connection(FilePath)
        print(f"CSV File : {FileName} data loaded successfully.\n")
        return csv_file

    except Exception as ex:
        print("CSV File is not loaded Successfully: \n", ex)
        return None
