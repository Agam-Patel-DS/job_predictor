import os

def create_directory(directory_path):
    try:
        # Create the directory along with any intermediate directories if they don't exist
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory '{directory_path}' created successfully!")
    except Exception as e:
        print(f"Error creating directory '{directory_path}': {e}")


import yaml

def read_yaml(file_path):
    """
    Reads a YAML file and returns its contents as a dictionary.

    :param file_path: Path to the YAML file.
    :return: Dictionary containing YAML data.
    """
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except yaml.YAMLError as e:
        print(f"Error reading YAML file {file_path}: {e}")

    return None
