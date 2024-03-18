import pandas as pd


def input_from_console():
    """
    Function for inputting data from console.

    Returns:
        str. data from console.
    """
    text = input("Write text: ")
    return text


def input_from_file(filename):
    """
    Function for inputting data from file using Python functions.

    Args:
        filename (str): Filepath.

    Returns:
        str. File content.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        return "File was not found."


def input_from_file_pandas(filename):
    """
    Function for inputting data from file using Pandas library.

    Args:
        filename (str): Filepath.

    Returns:
        str: File content.
    """
    try:
        data = pd.read_csv(filename)
        text = " ".join(data.values.flatten().astype(str))
        return text
    except FileNotFoundError:
        return "File was not found."
    except pd.errors.EmptyDataError:
        return ""

