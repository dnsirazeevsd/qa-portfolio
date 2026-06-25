from src.profile_user import get_user_status

def test_user(mocker):

    mocker_response = mocker.Mock()

    mocker_response.json.return_value = {"status" : "OK"}

    mocker.patch('src.profile_user.requests.get', return_value=mocker_response)

    result = get_user_status(123)

    assert result["status"] == "OK"