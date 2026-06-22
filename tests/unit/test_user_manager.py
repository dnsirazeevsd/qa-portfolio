import pytest

#Добавление нового пользователя
@pytest.mark.parametrize("username, password", 
    [
        ("user1", "123"),
        ("user2", "abc"),
        ("test", "pass")
    ])
def test_register_user(user_manager, username, password):
    user_manager.register_user(username, password)

    assert username in user_manager.users
    assert user_manager.users[username] == password

#Проверка добавления уже существующего пользователя
def test_register_user_negative(user_manager_filled):
    with pytest.raises(ValueError, match= "User already exists"):
        user_manager_filled.register_user("admin", "12345")

#Проверка успешного авторизации пользователя
def test_login(user_manager_filled):
    assert user_manager_filled.login("danil", "qwerty")

#Проверка авторизации(пользователя не существует)
def test_login_user_not(user_manager):
    with pytest.raises(ValueError, match = "User not found"):
        user_manager.login("TEST", "TEST")

#Проверка авторизации(некорретных пароль)
def test_login_password_incorrect(user_manager_filled):
    with pytest.raises(ValueError, match = "Incorrect password"):
        user_manager_filled.login("admin", "123")

#Удаление существующего пользователя
def test_remove_user(user_manager_filled):
    user_manager_filled.delete_user("admin")

    assert user_manager_filled.user_exists("admin") is False

#Удаление несуществующего пользователя
def test_remove_user_not(user_manager):
    with pytest.raises(ValueError, match= "User not found"):
        user_manager.delete_user("admin")

#Проверка наличия пользователей
@pytest.mark.parametrize("username", 
    [   "admin",
        "danil"
])
def test_exists_users(user_manager_filled, username):
    assert user_manager_filled.user_exists(username)

@pytest.mark.parametrize("username",
[
    "Emil",
    "Ashot"                             
])
def test_exists_users_not(user_manager, username):
    assert user_manager.user_exists(username) is False