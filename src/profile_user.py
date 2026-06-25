import requests

def get_user_status(user_id):
    response = requests.get(f"https://example.com/{user_id}")

    data = response.json()
    return data