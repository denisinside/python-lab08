from app.io import input
from app.io import output
from tests import test_input


def main():
    text = input.input_from_console()

    output.output_to_console("From console: " + text)

    output.output_to_file(text, 'data//test_python.txt')

    text_from_file_builtin = input.input_from_file('data//test_python.txt')

    output.output_to_console("From file builtin: " + text_from_file_builtin)

    output.output_to_file_pandas(text_from_file_builtin, 'data//test_pandos.csv')

    text_from_file_pandas = input.input_from_file_pandas('data//test_pandos.csv')

    output.output_to_console("From file pandas: " + text_from_file_pandas)


if __name__ == "__main__":
    main()
