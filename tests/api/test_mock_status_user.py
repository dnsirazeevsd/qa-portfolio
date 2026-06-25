import pytest
from src.profile_user import get_user_status

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

    mocker.patch('src.profile_user.requests.get', return_value = mock_response)

    response = get_user_status(12)

    assert response.status_code == 404
    assert response.json()["error"] == "User not found"

#Проверка исключения через side-effect
def test_user_raises(mocker):
    
    mocker.patch('src.profile_user.requests.get', side_effect=TimeoutError("Request timeout"))

    with pytest.raises(TimeoutError, match="Request timeout"):
        get_user_status(1)