import pandas as pd

def extract(file_path):
    """
    Extract data from a CSV file.
    
    :param file_path: Path to the CSV file
    :return: DataFrame containing the extracted data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

def transform(data):
    """
    Transform the extracted data.
    
    :param data: DataFrame containing the extracted data
    :return: DataFrame containing the transformed data
    """
    try:
        # Example transformation: drop rows with missing values
        transformed_data = data.dropna()
        return transformed_data
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None

def load(data, output_path):
    """
    Load the transformed data into a new CSV file.
    
    :param data: DataFrame containing the transformed data
    :param output_path: Path to the output CSV file
    """
    try:
        data.to_csv(output_path, index=False)
        print(f"Data successfully loaded to {output_path}")
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    # Example usage
    input_file_path = 'path/to/input.csv'
    output_file_path = 'path/to/output.csv'
    
    # Extract
    data = extract(input_file_path)
    
    if data is not None:
        # Transform
        transformed_data = transform(data)
        
        if transformed_data is not None:
            # Load
            load(transformed_data, output_file_path)