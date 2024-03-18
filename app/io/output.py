import pandas as pd


def output_to_console(text):
    """
    Function for outputting data to console.

    Args:
        text (str): data for output.
    """
    print(text)
    return None


def output_to_file(text, filename):
    """
    Function for outputting data to file using Python functions.

    Args:
        text (str): data for outputting.
        filename (str): Filepath.
    """
    with open(filename, 'w') as file:
        file.write(text)
    return None


def output_to_file_pandas(text, filename):
    """
    Function for outputting data to file using Pandas library.

    Args:
        text (str): data for outputting.
        filename (str): Filepath.
    """
    data = pd.DataFrame([text])
    data.to_csv(filename)
    return None
