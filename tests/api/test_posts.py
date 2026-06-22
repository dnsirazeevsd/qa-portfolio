import pytest
import requests
from faker import Faker 

def test_posts(logged_request):
    fake = Faker()
    
    obj = {
        "title" : fake.sentence(),
        "body": fake.text(),
        "userId": 1
    }

    response = logged_request("/posts", "POST", json=obj)
    assert response.json()["title"] == obj["title"]
    assert response.json()["body"] == obj["body"]
    assert response.json()["userId"] == obj["userId"]
