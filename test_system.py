import json
import requests

def test_code():
    r = requests.get("http://localhost:8085")
    json_response = r.json()
    assert(json_response["code"] == 404)

def test_message():
    r = requests.get("http://localhost:8085")
    json_response = r.json()
    assert(json_response["message"] == "HTTP 404 Not Found")