import psycopg2
from main import *
from init import InitDB
from config import *
import json
import pytest
from xml.dom import minidom


def test_connection_init_db_if_correct_dot_env_config_values_exists_in_db():
    init = InitDB(creds['HOST'], creds['DBNAME'], creds['USER'], creds['PASSWORD'])
    with init.init_connector().cursor() as cur:
        cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' "
                    "AND schemaname != 'information_schema';")
        assert cur.fetchall() is not None


def test_creating_schema():
    queries = QueriesDB(creds['HOST'], creds['DBNAME'], creds['USER'], creds['PASSWORD'])
    assert queries.create_schema() == "Schema created!"


def test_mini_atomicity_frm_files_to_db_and_first_query():
    rooms_frm_input, rooms_frm_output = open('data/in/rooms.json'), \
        open('data/out/query_1.json')
    data_in, data_out = json.load(rooms_frm_input), json.load(rooms_frm_output)
    assert len(data_out['column_1']) == len(data_in)


def test_second_query_result_try():
    query_2 = open('data/out/query_2.json')
    data = json.load(query_2)
    assert len(data["column_0"]) == len(data["column_1"]) == 5


def test_third_query_result_try():
    query_3 = open('data/out/query_3.json')
    data = json.load(query_3)
    assert len(data["column_0"]) == len(data["column_1"]) == 5


def test_fourth_query_result_try():
    query_json, query_xml = open('data/out/query_4.json'), \
        open('data/out/query_4.xml')
    data_json = json.load(query_json)
    data_xml = minidom.parse(query_xml)
    data_xml_ready = data_xml.getElementsByTagName('index')
    assert len(data_json["column_1"]) == len(data_xml_ready)






