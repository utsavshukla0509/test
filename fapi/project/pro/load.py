import json

import pandas as pd
from sqlalchemy.orm import sessionmaker

from database import engine
from model import geojson

#
# from fapi.project.pro.model import geojson

session = sessionmaker(bind=engine)
session = session()

# LOAD CSV data into database(postgres)------->table name = pincode
data = pd.read_csv('data.csv')
data = data.values
pin = ""
add = ""
ci = ""
lat = 0
long = 0
# for i in range(data.shape[0]):
#     pin = data[i][0]
#     add = data[i][1]
#     ci = data[i][2]
#     lat = data[i][3]
#     long = data[i][4]
#     # print(pin,add,ci,lat,long)
#     obj = pincode(pincode=pin, address=add, city=ci, latitude=lat, longitude=long)
#     session.add(obj)
# session.commit()

# latma = data[0][3]
# latmi = data[0][3]
# lonma = data[0][4]
# lonmi = data[0][4]
#
# for i in range(1, data.shape[0]):
#     latma = max(data[i][3], latma)
#     latmi = min(data[i][3], latmi)
#     lonma = max(data[i][4], lonma)
#     lonmi = min(data[i][4], lonmi)
#
# print(latmi, latma, lonmi, lonma)

latmi = 21.6833
latma = 30.25
lonmi = 72.2833
lonma = 92.35

# LOAD JSON data into database(postgres) --------> table name = geojson


# with open('json_path') as f:
#     data = json.load(f)
#
# name = ""
# type = ""
# parent = ""
# all_lon_lat = []
# n = 0
# lat = 0
# lon = 0
# for value in data["features"]:
#     for key, val in value.items():
#         coor = []
#         if key == "properties":
#             for all_key, all_val in val.items():
#                 if all_key == "name":
#                     name = all_val
#                 if all_key == "type":
#                     type = all_val
#                 if all_key == "parent":
#                     parent = all_val
#             # print(name, type, parent)
#         if key == "geometry":
#             for all_key, all_val in val.items():
#                 if all_key == "coordinates":
#                     all_lon_lat = all_val[0]
#                     n = len(all_lon_lat)
#                     for i in range(n):
#                         lat = all_lon_lat[i][0]
#                         lon = all_lon_lat[i][1]
#                         ans = [lat, lon]
#                         coor.append(ans)
#                     # print(name, type, parent, coor)
#                     obj = geojson(name=name, type=type, parent=parent, coordinates=coor)
#                     session.add(obj)
# session.commit()