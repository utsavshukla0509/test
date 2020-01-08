import sqlalchemy
from sqlalchemy import Column,create_engine
from sqlalchemy import FLOAT,VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class pincode(Base):
    __tablename__ = 'pincode'
    pincode = Column('pincode',VARCHAR, primary_key=True)
    address = Column('address', VARCHAR)
    city = Column('city', VARCHAR)
    latitude = Column('latitude', FLOAT)
    longitude = Column('longitude', FLOAT)


def __repr__(self):
    return "<pincode(pincode='{}', address='{}',city='{}',latitude={},longitude={})>".format(self.pincode, self.address,
                                                                                             self.city, self.latitude,
                                                                                             self.longitude)


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/pincode"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
conn = engine.connect()

try:
    print('your connection ok \n connection object is:{}'.format(conn))
except:
    print('your connection not connected')

Base.metadata.create_all(bind=engine)
