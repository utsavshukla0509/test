import pytest
from sqlalchemy.orm import Session, sessionmaker

import crud
import schemas
from database import engine


@pytest.fixture
def db():
    print("SETUP")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def test_get_data(db, lat=28.6333, lon=77.2167):
    items = crud.get_items(db, lat, lon)
    print("okkk")
    assert items["pincode"] == "IN/110001"
    assert items["address"] == "Connaught Place"
    assert items["city"] == "New Delhi"


def test_post_data(db, pin='IN/110001', add='Connaught Place', ci='New Delhi', lat=28.6333, lon=77.2167):
    with pytest.raises(Exception):
        user = schemas.User()
        user.pincode = pin
        user.address = add
        user.city = ci
        user.latitude = lat
        user.longitude = lon
        assert crud.post_items(db, user) == "item already existed"


def test_fetch_city(db, lat=28.6167, lon=77.2167):
    with pytest.raises(Exception):
        user = schemas.Userin()
        user.latitude = lat
        user.longitude = lon
        assert crud.fetch_city(db, user) == {"name": "Greater Noida"}
