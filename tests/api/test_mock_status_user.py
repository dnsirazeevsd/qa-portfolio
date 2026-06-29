import pytest
from src.profile_user import get_user_status, upload_user_files

#Проверка status 200 - mock
def test_user_200(mocker):

    mocker_response = mocker.Mock()

    mocker_response.json.return_value = {"status" : "OK"}
    mocker_response.status_code = 200

    mocker.patch('src.profile_user.requests.get', return_value=mocker_response)

    response = get_user_status(123)

    assert response.status_code == 200
    assert response.json()["status"] == "OK"

#Проверка status 500 - mock
def test_user_500(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"error": "server error"}

    mocker.patch('src.profile_user.requests.get', return_value = mock_response)

    response = get_user_status("TEST")

    assert response.status_code == 500
    assert response.json()["error"] == "server error"

#Проверка status 404 - mock
def test_user_404(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"error": "User not found"}

    mock_get = mocker.patch('src.profile_user.requests.get', return_value = mock_response)

    response = get_user_status(12)

    #Проверка корректно вызова функции с корретными данными + что вызвали ровно 1 раз
    mock_get.assert_called_once_with("https://example.com/12")

    assert response.status_code == 404
    assert response.json()["error"] == "User not found"

#Проверка исключения через side-effect
def test_user_raises(mocker):
    
    mocker.patch('src.profile_user.requests.get', side_effect=TimeoutError("Request timeout"))

    with pytest.raises(TimeoutError, match="Request timeout"):
        get_user_status(1)

#Проверка загрузки файлов пользователя - mock 200
def test_upload_user_files_200(mocker):

    files = {"avatar": ("avatar.png", b"fake_image_bytes"), "document": ("file.pdf", b"fake_pdf_bytes")}

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "files uploaded"}

    mock_post = mocker.patch('src.profile_user.requests.post', return_value=mock_response)

    response = upload_user_files(1, files)

    assert response.status_code == 200
    assert response.json()["status"] == "files uploaded"

    mock_post.assert_called_once_with(
        "https://example.com/1/files",
        files=files
    )
