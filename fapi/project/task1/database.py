from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# import psycopg2
Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/pincode"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
conn = engine.connect()

try:
    print('your connection ok \n connection object is:{}'.format(conn))
except:
    print('your connection not connected')

# Base.metadata.create_all(engine)
