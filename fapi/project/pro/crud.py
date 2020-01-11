from math import *
import load
import numpy as np
from sqlalchemy.orm import Session, sessionmaker
import model
import schemas
from database import engine

from django_earthdistance.models import EarthDistanceQuerySet

from json_demo import mapping


def get_items(db: Session, lat: float, lon: float):
    items = db.query(model.pincode.pincode, model.pincode.address, model.pincode.city).filter(
        model.pincode.latitude == lat, model.pincode.longitude == lon).first()
    v = list(items)
    # print(v)
    k = ["pincode", "address", "city"]
    items = zip(k, v)
    items = dict(items)
    return items


def post_items(db: Session, user: schemas.User):
    db_user = model.pincode(pincode=user.pincode, address=user.address, city=user.city, latitude=user.latitude,
                            longitude=user.longitude)
    db.add(db_user)
    try:
        db.commit()
    except:
        return {"item already existed"}

    db.refresh(db_user)
    return {"operation successful"}


def get_pins_by_self(db: Session, rad: float, lat: float, lon: float):
    total_pin = []
    rows = db.query(model.pincode.pincode, model.pincode.latitude, model.pincode.longitude).all()
    for row in rows:
        if (row.latitude >= load.latmi) and (row.latitude <= load.latma) and (row.longitude >= load.lonmi) and (
                load.lonma >= row.longitude):
            dist = float(acos(sin(lat) * sin(row.latitude) + cos(lat) * cos(row.latitude) * cos(
                row.longitude - lon)) * 6371)
            if dist <= rad:
                items = db.query(model.pincode.pincode).filter(
                    model.pincode.latitude == row.latitude, model.pincode.longitude == row.longitude).first()
                v = [str(items)]
                k = ["pincode"]
                items = zip(k, v)
                total_pin.append(items)
    return total_pin


# def get_pins_by_postgres(db: Session, rad: float, lat: float, lon: float):
#     total_pin = []
#     objects = EarthDistanceQuerySet.as_manager()
#     conn = engine.connect()
#     items = db.query(model.pincode.pincode).whereclause(
#         earth_distance(LlToEarth([model.pincode.latitude, model.pincode.longitude]),
#                       LlToEarth([lat, lon])) < rad)
#     print(items)
#     return {}

#


def fetch_city(db: Session, user: schemas.Userin):
    map = mapping
    main_map = {}
    for key, val in map.items():
        lat = val[0]
        lon = val[1]
        dist = float(acos(sin(user.latitude) * sin(lat) + cos(user.latitude) * cos(lat) * cos(
            lon - user.longitude)) * 6371)
        main_map[key] = dist
    main_map = {k: v for k, v in sorted(main_map.items(), key=lambda item: item[1], reverse=True)}
    # print(type(list(main_map.keys())[0]))
    return {"name": list(main_map.keys())[0]}
