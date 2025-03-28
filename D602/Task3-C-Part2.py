import pytest
from fastapi.testclient import TestClient
from API import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is functional!"}

def test_predict_delays_correct_format():
    response = client.get("/predict/delays", params={
        "arrival_airport": "JFK",
        "departure_airport": "LAX",
        "departure_time": "2025-03-03T08:00:00",
        "arrival_time": "2025-03-03T16:00:00"
    })
    assert response.status_code == 200
    assert "average_departure_delay" in response.json()

def test_predict_delays_incorrect_format():
    response = client.get("/predict/delays", params={
        "arrival_airport": "JFK",
        "departure_airport": "LAX",
        "departure_time": "invalid-time-format",
        "arrival_time": "2025-03-03T16:00:00"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid time format. Please use 'YYYY-MM-DDTHH:MM:SS'."}

def test_predict_delays_missing_airport():
    response = client.get("/predict/delays", params={
        "arrival_airport": "INVALID",
        "departure_airport": "LAX",
        "departure_time": "2025-03-03T08:00:00",
        "arrival_time": "2025-03-03T16:00:00"
    })
    assert response.status_code == 404
    assert response.json() == {"detail": "Arrival airport not found"}

# Additional tests to demonstrate progression

def test_predict_delays_future_date():
    response = client.get("/predict/delays", params={
        "arrival_airport": "JFK",
        "departure_airport": "LAX",
        "departure_time": "2030-03-03T08:00:00",
        "arrival_time": "2030-03-03T16:00:00"
    })
    assert response.status_code == 200
    assert "average_departure_delay" in response.json()

def test_predict_delays_past_date():
    response = client.get("/predict/delays", params={
        "arrival_airport": "JFK",
        "departure_airport": "LAX",
        "departure_time": "2010-03-03T08:00:00",
        "arrival_time": "2010-03-03T16:00:00"
    })
    assert response.status_code == 200
    assert "average_departure_delay" in response.json()

def test_predict_delays_same_airport():
    response = client.get("/predict/delays", params={
        "arrival_airport": "JFK",
        "departure_airport": "JFK",
        "departure_time": "2025-03-03T08:00:00",
        "arrival_time": "2025-03-03T16:00:00"
    })
    assert response.status_code == 200
    assert "average_departure_delay" in response.json()