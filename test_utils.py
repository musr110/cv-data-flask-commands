import unittest

from utils import extract_year, filter_data


class TestCVFunctions(unittest.TestCase):

    # test the extract_year function
    def test_extract_year(self):
        my_json = {"start_date": "2019-01-01"}
        result = extract_year(my_json)
        self.assertEqual(result, 2019)

        my_json = {"end_date": "2019-01-01"}
        result = extract_year(my_json)
        self.assertEqual(result, None)

    # test the filter_data function
    def test_filter_data(self):
        data = [
            {"start_date": "2019-01-01", "title": "Software Developer"},
            {"start_date": "2018-01-01", "title": "Senior Software Engineer"},
        ]
        result = filter_data(data, 2019)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Software Developer")

        result = filter_data(data, 2018)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Senior Software Engineer")

        result = filter_data(data, 2020)
        self.assertEqual(len(result), 0)

    # test the filter_data function with string as year argument
    def test_filter_data_string(self):
        data = [
            {"start_date": "2019-01-01", "title": "Software Developer"},
            {"start_date": "2018-01-01", "title": "Senior Software Engineer"},
        ]
        result = filter_data(data, "2019")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Software Developer")


if __name__ == "__main__":
    unittest.main()
