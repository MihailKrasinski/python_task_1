from dotenv import load_dotenv, dotenv_values
from sqlalchemy import create_engine

load_dotenv()
creds = dotenv_values(".env")

# # Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("postgresql+psycopg2://{user}:{pw}@{host}/{db}"
                       .format(host=creds['HOST'], db=creds['DBNAME'], user=creds['USER'],
                               pw=creds['PASSWORD']))

