from faker import Faker

import requests

from lesson6.Urls import Urls

fake = Faker()
urls = Urls()

def test_get_bookings():
    response = requests.get(urls.URL)
    assert response.status_code == 200

def test_create_bookings(create_booking):
    booking_id = create_booking["bookingid"]
    response_get_by_id = requests.get(f"{urls.URL}/{booking_id}")
    assert create_booking["booking"]["firstname"] == response_get_by_id.json()["firstname"] and create_booking["booking"]["lastname"] == response_get_by_id.json()["lastname"]


def test_update_booking(create_booking, get_token):
    booking_id = create_booking["bookingid"]
    update_data = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name()
    }
    requests.patch(f"{urls.URL}/{booking_id}", json=update_data, headers={"Cookie": f"token={get_token}"})
    response_get_by_id = requests.get(f"{urls.URL}/{booking_id}")
    assert update_data["firstname"] == response_get_by_id.json()["firstname"] and update_data["lastname"] == response_get_by_id.json()["lastname"]

def test_delete_booking(get_token, create_booking):
    booking_id = create_booking["bookingid"]
    requests.delete(f"{urls.URL}/{booking_id}", headers={"Cookie": f"token={get_token}"})
    assert requests.get(f"{urls.URL}/{booking_id}").status_code == 404