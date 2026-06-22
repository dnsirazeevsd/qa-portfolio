class UserManager:
    #Конструктор по умолчанию
    def __init__(self):
        self.users = {}

    #Добавление нового пользователя
    def register_user(self, username, password):
        if username in self.users:
            raise ValueError("User already exists")
        
        self.users[username] = password

    #Удаление пользователя
    def delete_user(self, username):
        if username not in self.users:
            raise ValueError("User not found")
        
        self.users.pop(username)

    #Вход в аккаунт
    def login(self, username, password):
        if username not in self.users:
            raise ValueError("User not found")
        
        if self.users[username] != password:
            raise ValueError("Incorrect password")
        
        return True
    
    #Проверка наличия аккаунта поьзователя
    def user_exists(self, username):
        return username in self.users