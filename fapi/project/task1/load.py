import pandas as pd
from sqlalchemy.orm import sessionmaker
from database import engine
from models import pincode

session = sessionmaker(bind=engine)
session = session()
data = pd.read_csv('data.csv')
data = data.values
pin = ""
add = ""
ci = ""
lat = 0
long = 0
for i in range(data.shape[0]):
    pin = data[i][0]
    add = data[i][1]
    ci = data[i][2]
    lat = data[i][3]
    long = data[i][4]
    # print(pin,add,ci,lat,long)
    obj = pincode(pincode=pin, address=add, city=ci, latitude=lat, longitude=long)
    session.add(obj)
session.commit()
