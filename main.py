from api_query import rest_create_json
from api_query import etl_write_to_db
from db_data import ret_db_data


def test_regresion():
    rest_data = rest_create_json()  # rest api generated data
    etl_write_to_db()
    db_data = ret_db_data()
    #TODO:
    # The first line generates json
    # The second line runs etl and writes the modified data to the database
    # The third line collects data from the database. (The function in the third line fails to query the database.)
    # The data are not in the same format, so the analysis would require further editing of the data obtained in this function.
    # That wouldn't be a big deal.


if __name__ == "__main__":
    test_regresion()