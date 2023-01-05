from psycopg2 import connect
from sqlalchemy import create_engine


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
