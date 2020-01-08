from fastapi import HTTPException
from sqlalchemy.orm import Session


import models
import schemas
from database import engine


def get_items(db: Session, lat: float, lon: float):
    items = db.query(models.pincode.pincode, models.pincode.address, models.pincode.city).filter(
        models.pincode.latitude == lat, models.pincode.longitude == lon).first()
    v = list(items)
    k = ["pincode", "address", "city"]
    items = zip(k, v)
    items = dict(items)
    return items


def post_items(db: Session, user: schemas.User):
    db_user = models.pincode(pincode=user.pincode, address=user.address, city=user.city, latitude=user.latitude,
                             longitude=user.longitude)
    db.add(db_user)
    try:
        db.commit()
    except:
        return HTTPException(status_code=400, detail="item already existed")

    db.refresh(db_user)
    return {"operation successful"}
