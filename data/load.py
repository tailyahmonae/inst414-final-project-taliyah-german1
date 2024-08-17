import json

def save_to_file(data, filename):
    """
    save the data to a JSON file

    Args:
        data (dict): he data to save
        filename (str): name of the file to save the data to
    """
    
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_from_file(filename):
    """
    load data from a JSON file

    Args:
        filename (str): name of the file to load the data from

    Returns:
        dict: data loaded from the file
    """
    
    with open(filename, 'r') as f:
        return json.load(f)
