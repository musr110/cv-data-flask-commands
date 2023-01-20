"""Module for utilities components"""


def extract_year(my_json):
    """Extract year from my_json"""
    if "start_date" in my_json:
        return int(my_json["start_date"].split("-")[0])
    else:
        return None


def filter_data(data, year):
    """
    Filter data by year
    """
    # overcome this example test so that I can use both request obj and path parameter to work.
    if not isinstance(year, int):
        year = int(year)
    return [x for x in data if extract_year(x) == year]
