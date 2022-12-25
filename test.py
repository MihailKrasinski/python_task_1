from main import *
from config import *
import json
import pytest


# WARNING::: NEED TO RUN TESTS ONLY AFTER COMPLETING PUT DATA TO DATABASE
def test_atomicity_frm_files_to_db():
    file_1, file_2 = open('/home/mikra/MikraPythonProjects/python_task_1/data/in/rooms.json'), \
        open('/home/mikra/MikraPythonProjects/python_task_1/data/in/students.json')
    data_1, data_2 = json.load(file_1), json.load(file_2)
    data_input_file_1_len, data_input_file_2_len = len(data_1), len(data_2)
    test_queries_session = QueriesDB(creds['HOST'], creds['DBNAME'], creds['USER'], creds['PASSWORD'])
    test_query_rooms_all, test_query_students_all = 'SELECT * FROM rooms;', 'SELECT * FROM students;'
    data_output_frm_db_len_file_1, data_output_frm_db_len_file_2 = \
        len(test_queries_session.req_query_out(test_query_rooms_all)), \
        len(test_queries_session.req_query_out(test_query_students_all)),
    assert data_input_file_1_len == data_output_frm_db_len_file_1
    assert data_input_file_2_len == data_output_frm_db_len_file_2





