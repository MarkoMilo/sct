import http_client as http_cl
import json

# MACROS
GET_STATUS_SUCCESS = 200
GET_REASON_SUCCESS = 'OK'
GET_STATUS_FAILED = 400
GET_REASON_FAILED = 'OK'

POST_STATUS_SUCCESS = 201
POST_REASON_SUCCESS = 'Created'
POST_STATUS_FAILED = 400
POST_REASON_FAILED = 'Bad Request'

PORT = 9090
DEVICE_IP = "127.0.0.1"
REST_API_URL = '?ids=1,2,3&user_ids=1,2'
ETL_API_URL = '/run?ids=1,2,3&user_ids=1,2'
REST_API_PORT = 9090
ETL_API_PORT = 9091
ADMINER_API_PORT = 9092


def http_cli(device_ip=DEVICE_IP, port=PORT):
    client = http_cl.HttpClient(device_ip, port)
    return client


def rest_create_json(table="/shifts"):
    """
    Function call rest api and generates json
    assert check if the call is successful
    :param table: table in database, default shifts
    :return: return list that contains json
    """
    client = http_cli(DEVICE_IP, REST_API_PORT)
    # GET
    db_table_url = "/{}{}".format(table, REST_API_URL)
    get_data, get_status = client.http_api_get(db_table_url)
    print("\nGet data: {}\n".format(get_data))
    assert get_status.status == GET_STATUS_SUCCESS
    return get_data, get_status


def etl_write_to_db():
    """
    Function call etl API, transform JSON and write it into the database
    assert check if the call is successful
    :return:
    """
    client = http_cli(DEVICE_IP, ETL_API_PORT)
    # GET
    get_data, get_status = client.http_api_get(ETL_API_URL)
    print("\nGet Status: {}\n".format(get_status))
    assert get_status.status == GET_STATUS_SUCCESS
    return get_data, get_status



