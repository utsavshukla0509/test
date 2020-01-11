from typing import List

import uvicorn
from database import engine
from sqlalchemy.orm import Session, sessionmaker
from fastapi import FastAPI, Depends, HTTPException

import crud
import schemas
import model

model.Base.metadata.create_all(engine)
app = FastAPI()


def get_db():
    try:
        session = sessionmaker(bind=engine)
        # session.configure(engine)
        db = session()
        yield db
    finally:
        db.close()


@app.get("/get_location/{lat}/{lon}", response_model=schemas.Userout)
async def read_user(lat: float, lon: float, db: Session = Depends(get_db)):
    # print("success")
    items = crud.get_items(db, lat=lat, lon=lon)
    # print("-------",items,"-----------")
    return items


@app.post("/post_location/")
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.post_items(db, user)


@app.get("/get_using_self/{rad}/{lat}/{lon}", response_model=List[schemas.allpin])
async def fetch_pin_by_self(rad: float, lat: float, lon: float, db: Session = Depends(get_db)):
    return crud.get_pins_by_self(db, rad=rad, lat=lat, lon=lon)


#
# @app.get("/get_using_postgres/{rad}/{lat}/{lon}", response_model=List[schemas.allpin])
# async def fetch_pin_by_postgres(rad: float, lat: float, lon: float, db: Session = Depends(get_db)):
#     return crud.get_pins_by_postgres(db, rad=rad, lat=lat, lon=lon)

@app.get("/detect/{lat}/{lon}", response_model=schemas.place)
async def get_city_name(lat: float, lon: float, db: Session = Depends(get_db)):
    user = schemas.Userin
    user.latitude = lat
    user.longitude = lon
    return crud.fetch_city(db, user)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port="8000")
