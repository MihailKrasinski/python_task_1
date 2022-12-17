from sql_queries import *
import pandas as pd
from psycopg2 import connect
from config import creds, engine


def connector():
    connection = connect(
        host=creds['HOST'],
        user=creds['USER'],
        password=creds['PASSWORD'],
        database=creds['DBNAME']
    )
    connection.autocommit = True
    return connection


def disconnect():
    connector().cursor().close()
    connector().close()


def create_schema(query):
    cursor = connector().cursor()
    cursor.execute(query)
    disconnect()


def req_query_out(query):
    cursor = connector().cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    disconnect()
    return res


def json_to_sql(table, dir_json_file):
    df = pd.read_json(dir_json_file)
    df.to_sql(table, engine, index=False, if_exists='append')


create_schema(schema)

# filling tables
json_to_sql('rooms', '/home/mikra/MikraPythonProjects/python_task_1/data/in/rooms.json')
json_to_sql('students', '/home/mikra/MikraPythonProjects/python_task_1/data/in/students.json')

print(req_query_out(query_1))
print(req_query_out(query_2))
print(req_query_out(query_3))
print(req_query_out(query_4))



