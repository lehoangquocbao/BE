import requests

def test_get_users():
    res = requests.get("http://127.0.0.1:5000/users")
    assert res.status_code == 200