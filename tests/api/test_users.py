import pytest

#Проверки пользователя(статус 200, id совпадает с параметром)
@pytest.mark.parametrize("id_user", 
[
    1, 2, 3, 4, 5
])
def test_users_id(logger_request, id_user):
    response = logger_request(f"/users/{id_user}", "GET")
    assert response.status_code == 200
    assert response.json()["id"] == id_user

#Проверка наличие полей у обьекта user
def test_user_struct(logger_request):
    response = logger_request("/users/1", "GET")
    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data

#Проверка типа полей обьекта user
def test_user_type(logger_request):
    response = logger_request("/users/1", "GET")
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)

#Проверка запроса несуществующего пользователя(негатив)
def test_user_negative(logger_request):
    response = logger_request("/users/999")

    assert response.status_code == 404

#Проверка полей обьекта через параметизацию
@pytest.mark.parametrize("field", 
[
    "id",
    "name",
    "username",
    "email"
])
def test_user_field(return_json, field):
   
    assert field in return_json