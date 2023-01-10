import logging
from psycopg2 import connect
from sqlalchemy import create_engine


class InitDB:
    """
    The InitDB class is a utility class that contains various
    methods for interacting with a PostgreSQL database.
    It has methods: __init__, engine, cinit_connector,
    disconnect.
    Args:
        config: credentials to connect to database(str)
    Attributes:
        host: DB Host
        database: DB name
        user: DB user
        password: DB password
    """
    def __init__(self, host: str, db: str, user: str, password: str):
        """
        Connection Attributes

        Args:
            config: credentials to connect
        """
        self.host = host
        self.database = db
        self.user = user
        self.password = password

    def engine(self):
        """
        Create engine to work with database

        Returns:
            Engine object
        """
        return create_engine("postgresql+psycopg2://{user}:{pw}@{host}/{db}"
                             .format(host=self.host, db=self.database, user=self.user,
                                     pw=self.password))

    def init_connector(self):
        """
        Create connection to connect the database to work with cursor after

        Returns:
            Connection
        """
        connection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        connection.autocommit = True
        logging.debug("Session connection initialised!")
        return connection

    def disconnect(self):
        """
        Disconnecting cursor session with db
        """
        self.init_connector().cursor().close()
        self.init_connector().close()
        logging.debug("Session connection disconnected!")
