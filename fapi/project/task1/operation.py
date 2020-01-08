from typing import List

import uvicorn
from database import engine
from sqlalchemy.orm import Session, sessionmaker
from fastapi import FastAPI, Depends, HTTPException

import crud
import schemas
import models

models.Base.metadata.create_all(engine)
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
    print("success")
    items = crud.get_items(db, lat=lat, lon=lon)
    # print("-------",items,"-----------")
    return items


@app.post("/post_location/")
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.post_items(db, user)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port="8000")
