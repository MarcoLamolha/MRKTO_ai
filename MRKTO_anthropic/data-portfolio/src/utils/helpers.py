# src/utils/helpers.py

def save_to_file(data, filename):
    """Saves data to a specified file."""
    with open(filename, 'w') as file:
        file.write(data)

def load_from_file(filename):
    """Loads data from a specified file."""
    with open(filename, 'r') as file:
        return file.read()

def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")