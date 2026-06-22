import pytest

#Добавление книги
@pytest.mark.parametrize("name_book", 
    [   "Harry Potter",
        "Clean Code",
        "Python Crash Course"])
def test_func_add_book(library, name_book):
    library.add_book(name_book)
    assert name_book in library.get_books() 
#Удаление книги
@pytest.mark.parametrize("name_book", 
    [   "Harry Potter",
        "1984",
        "The Hobbit"])
def test_remove_book(library_with_books, name_book):
    library_with_books.remove_book(name_book)
    assert name_book not in library_with_books.get_books()
#Удаление несуществующей книги(Негативный тест)
def test_remove_book_negative(library):
    with pytest.raises(ValueError, match="not found"):
        library.remove_book("TEST")
#Проверка кол-ва книг в библиотеки
def test_count_books(library_with_books):
    assert library_with_books.get_count_books() == 3
#Проверка если ли книга в библиотеки
@pytest.mark.parametrize("name_book", 
    [
        "Harry Potter",
        "1984",
        "The Hobbit"
])
def test_has_book(library_with_books, name_book):
    assert library_with_books.has_book(name_book) is True