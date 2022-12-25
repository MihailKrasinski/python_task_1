from sql_queries import *
from config import creds
from psycopg2 import connect
from sqlalchemy import create_engine
import pandas as pd
from loguru import logger


class InitDB:
    def __init__(self, host: str, db: str, user: str, password: str):
        self.host = host
        self.database = db
        self.user = user
        self.password = password

    def engine(self):
        return create_engine("postgresql+psycopg2://{user}:{pw}@{host}/{db}"
                             .format(host=self.host, db=self.database, user=self.user,
                                     pw=self.password))

    def init_connector(self):
        connection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        connection.autocommit = True
        return connection

    def disconnect(self):
        self.init_connector().cursor().close()
        self.init_connector().close()


class QueriesDB(InitDB):
    def create_schema(self, schem):
        cursor = super().init_connector().cursor()
        cursor.execute(schem)
        super().disconnect()

    def req_query_out(self, query):
        with super().init_connector().cursor() as cursor:
            cursor.execute(query)
            res = cursor.fetchall()
            super().disconnect()
            return res

    def json_to_sql(self, table, dir_json_file):
        df = pd.read_json(dir_json_file)
        df.to_sql(table, super().engine(), index=False, if_exists='append')

    def out_to_xml(self, query):
        df = pd.DataFrame(self.req_query_out(query),
                          columns=[f'column_{i + 1}' for i in range(len(self.req_query_out(query)[0]))])
        df.to_xml('data/out/xml_out.xml')

    def out_to_json(self, query):
        df = pd.DataFrame(self.req_query_out(query),
                          columns=[f'column_{i + 1}' for i in range(len(self.req_query_out(query)[0]))])
        df.to_json('data/out/json_out.json')


if __name__ == "__main__":
    @logger.catch
    def main():
        # log shows only that db already filled and data already exists
        logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB", compression="zip")
        # init = InitDB(creds['HOST'], creds['DBNAME'], creds['USER'], creds['PASSWORD'])
        queries = QueriesDB(creds['HOST'], creds['DBNAME'], creds['USER'], creds['PASSWORD'])
        queries.create_schema(schema)

        # filling tables
        queries.json_to_sql('rooms', '/home/mikra/MikraPythonProjects/python_task_1/data/in/rooms.json')
        queries.json_to_sql('students', '/home/mikra/MikraPythonProjects/python_task_1/data/in/students.json')

        # print result of SQL request query from DB
        print(queries.req_query_out(query_1))
        print(queries.req_query_out(query_2))
        print(queries.req_query_out(query_3))
        print(queries.req_query_out(query_4))

        # puts data of SQL query you ask to xml / JSON from DB
        queries.out_to_xml(query_3)
        queries.out_to_json(query_3)
    main()
