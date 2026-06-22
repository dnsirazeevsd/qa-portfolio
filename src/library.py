class Library:
    #Конструктор класса(пустой список книг)
    def __init__(self):
        self.books = []
    #Добваляем новую книгу
    def add_book(self, name_book):
        self.books.append(name_book)
    #Удаляем книгу, если ее нет - выкидываем исключение    
    def remove_book(self, name_book):
        if name_book not in self.books:
            raise ValueError("not found")
        
        self.books.remove(name_book)
    #Возвращаем список книг
    def get_books(self):
        return self.books
    #Возвращаем кол-во книг
    def get_count_books(self):
        return len(self.books)
    #Проверка есть ли книга в библиотеки
    def has_book(self, name_book):
        return name_book in self.books