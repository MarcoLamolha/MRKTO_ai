import pandas as pd
import sqlalchemy

def extract_from_csv(file_path):
    """
    Extract data from a CSV file.
    
    :param file_path: Path to the CSV file
    :return: DataFrame containing the extracted data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def extract_from_database(connection_string, query):
    """
    Extract data from a database.
    
    :param connection_string: Database connection string
    :param query: SQL query to execute
    :return: DataFrame containing the extracted data
    """
    try:
        engine = sqlalchemy.create_engine(connection_string)
        data = pd.read_sql_query(query, engine)
        return data
    except Exception as e:
        print(f"Error extracting data from database: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    csv_data = extract_from_csv('path/to/your/file.csv')
    db_data = extract_from_database('your_connection_string', 'SELECT * FROM your_table')
    
    print(csv_data.head())
    print(db_data.head())