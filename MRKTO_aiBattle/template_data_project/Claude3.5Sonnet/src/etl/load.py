import pandas as pd
import sqlalchemy

def extract(file_path):
    """
    Extract data from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def transform(data):
    """
    Transform the data.
    """
    # Example transformation: drop rows with missing values
    data = data.dropna()
    return data

def load(data, database_uri, table_name):
    """
    Load data into a database.
    """
    engine = sqlalchemy.create_engine(database_uri)
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)

if __name__ == "__main__":
    # Example usage
    file_path = 'path/to/your/csvfile.csv'
    database_uri = 'sqlite:///your_database.db'
    table_name = 'your_table_name'

    data = extract(file_path)
    data = transform(data)
    load(data, database_uri, table_name)