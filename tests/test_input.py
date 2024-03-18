import unittest
from app.io import input


class TestInputFunctions(unittest.TestCase):
    #  input_from_file
    def test_input_from_file_builtin_exists(self):
        result = input.input_from_file(r'C:\Users\denisinside\PycharmProjects\python-for-big-data-and-data-science'
                                       r'\pythonProject1\data\empty.txt')
        self.assertEqual(result, "")

    def test_input_from_file_builtin_correct(self):
        result = input.input_from_file(r'C:\Users\denisinside\PycharmProjects\python-for-big-data-and-data-science'
                                       r'\pythonProject1\data\pespatron.txt')
        self.assertEqual(result, "pespatron")

    def test_input_from_file_builtin_not_found(self):
        result = input.input_from_file('meowmeow.txt')
        self.assertEqual(result, "File was not found.")


    #  input_from_file_pandas
    def test_input_from_file_pandas_exists(self):
        result = input.input_from_file_pandas(r'C:\Users\denisinside\PycharmProjects\python-for-big-data-and-data'
                                              r'-science\pythonProject1\data\empty.csv')
        self.assertEqual(result, "")

    def test_input_from_file_pandas_correct(self):
        result = input.input_from_file_pandas(r'C:\Users\denisinside\PycharmProjects\python-for-big-data-and-data'
                                              r'-science\pythonProject1\data\pespatron.csv')
        self.assertEqual(result, "0 pespatron")

    def test_input_from_file_pandas_not_found(self):
        result = input.input_from_file_pandas('meowmeow.csv')
        self.assertEqual(result, "File was not found.")


if __name__ == '__main__':
    unittest.main()