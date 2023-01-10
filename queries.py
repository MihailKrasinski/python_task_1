from init import InitDB
import pandas as pd
from sqlalchemy import text
import logging


class QueriesDB(InitDB):
    """
    The QueriesDB class to complete database queries, that contains various
    methods to create database schema and attributes, class inherited from parent class of database connection InitDB.
    It has few methods: create schema, json_to_sql, queries_out.
    """
    def create_schema(self):
        """
        Creates database schema
        Args:
            text: SQL query wrapped in text method from SQL alchemy
        Returns:
            The method returns message: "Schema created!"
        """
        super().engine().execute(text('''
                create table if not exists rooms (
                    id int primary key,
                    name text
                );
                create table if not exists students (
                    birthday timestamp,
                    id int primary key,
                    name text,
                    room int,
                    sex varchar(1),
                    CONSTRAINT room_fk
                        FOREIGN key(room)
                            REFERENCES rooms(id)
                );
                '''))
        logging.debug("Schema created!")
        return "Schema created!"

    def json_to_sql(self, table, dir_json_file):
        """
        Writes DataFrame object into database
        Args:
            df: pandas DataFrame object
        Returns:
            Message Dataframe loaded to Database! if executed
        """
        df = pd.read_json(dir_json_file)
        df.to_sql(table, super().engine(), index=False, if_exists='append')
        logging.debug("Dataframe loaded to Database!")

    def queries_out(self):
        """
        Get DataFrame object and data from the database using SQL query to folder (data / out) files .json or .xml

        Returns:
            2 Files: .json and .xml after every query if executed
        """
        self.create_schema()
        self.json_to_sql('rooms', 'data/in/rooms.json')
        self.json_to_sql('students', 'data/in/students.json')
        with super().init_connector().cursor() as cursor:
            cursor.execute('select rooms.name, count(students.id) '
                           'from rooms FULL OUTER JOIN students on rooms.id = students.room '
                           'group by 1 order by 2 desc;')
            result_1 = cursor.fetchall()
            cursor.execute('select rooms.name, avg(now() - students.birthday) '
                           'from rooms inner join students on rooms.id = students.room '
                           'group by 1 '
                           'order by 2 asc limit 5;')
            result_2 = cursor.fetchall()
            cursor.execute('select rooms.name, max(students.birthday) - min(students.birthday) '
                           'from rooms '
                           'inner join students on rooms.id = students.room '
                           'group by 1 '
                           'order by 2 desc limit 5;')
            result_3 = cursor.fetchall()
            cursor.execute('select rooms.name, max(students.birthday) - min(students.birthday) '
                           'from rooms '
                           'inner join students on rooms.id = students.room '
                           'group by 1 '
                           'order by 2 desc limit 5;')
            cursor.execute('select rooms.name, count(distinct(students.sex)) '
                           'from rooms inner join students on rooms.id = students.room '
                           'group by 1 having count(distinct(students.sex)) = 2 '
                           'order by 1 asc;')
            result_4 = cursor.fetchall()
            super().disconnect()
            df_1 = pd.DataFrame(result_1, columns=[f'column_{i}' for i in range(len(result_1[0]))])
            df_1.to_xml('data/out/query_1.xml')
            df_1.to_json('data/out/query_1.json')
            logging.debug("First Query Ready!")
            df_2 = pd.DataFrame(result_2, columns=[f'column_{i}' for i in range(len(result_2[0]))])
            df_2.to_xml('data/out/query_2.xml')
            df_2.to_json('data/out/query_2.json')
            logging.debug("Second Query Ready!")
            df_3 = pd.DataFrame(result_3, columns=[f'column_{i}' for i in range(len(result_3[0]))])
            df_3.to_xml('data/out/query_3.xml')
            df_3.to_json('data/out/query_3.json')
            logging.debug("Third Query Ready!")
            df_4 = pd.DataFrame(result_4, columns=[f'column_{i}' for i in range(len(result_4[0]))])
            df_4.to_xml('data/out/query_4.xml')
            df_4.to_json('data/out/query_4.json')
            logging.debug("Fourth Query Ready!")

