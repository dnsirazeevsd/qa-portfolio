import requests

def get_user_status(user_id):
    response = requests.get(f"https://example.com/{user_id}")

    return response

def upload_user_files(user_id, files):
    """Отправляет файлы пользователя на сервер и возвращает ответ."""
    response = requests.post(f"https://example.com/{user_id}/files", files=files)
    return response
