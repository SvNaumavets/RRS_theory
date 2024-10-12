import random

import pytest
import requests
from requests import session

from lesson6.lesson6 import urls, fake


@pytest.fixture()
def get_token():
    data = {
        "username": "admin",
        "password": "password123"
    }
    return (requests
                .post(urls.URL_AUTH, json=data)
                .json()["token"])

@pytest.fixture(scope="session")
def create_booking():
    data = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": random.randint(100, 500),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-11-01",
            "checkout": "2024-11-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(urls.URL, json=data)
    return response.json()