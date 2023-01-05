from config import creds
from queries import QueriesDB

from loguru import logger


if __name__ == "__main__":
    @logger.catch
    def main():
        logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB", compression="zip")
        queries = QueriesDB(creds['HOST'], creds['DBNAME'], creds['USER'], creds['PASSWORD'])
        queries.queries_out()
    main()
