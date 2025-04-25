from library import Library
from book import Book

import pytest

my_library = Library()


###בדיקה שהפונקציה מוסיפה ספר חדש לרשימת הספרים במערכת
@pytest.mark.parametrize("title", "author",
                         [("title", "author"),
                          ("", "")])
def test_add_book(title, author):
    new_book = Book(title, author)
    my_library.add_book(new_book)
    assert new_book in my_library.books


### בדיקה שהפונקציה מוסיפה משתמש חדש לרשימת המשתמשים
@pytest.mark.user
@pytest.mark.parametrize("username",
                         ["username", ""])
def test_add_username(username):
    my_library.add_user(username)
    assert username in my_library.users


### בדיקה שהמערכת מונעת השאלת ספר כאשר הוא כבר נמצא בהשאלה.
def test_check_out_book():
    my_library.checked_out_books("yaffi", my_library.books[0])
    my_library.checked_out_books("yaffi", my_library.books[0])
    assert my_library.books[0].is_checked_out
    assert my_library.checked_out_books["yaffi"] == my_library.books[0]


### בדיקה שהמערכת מונעת החזרת ספר שלא הושאל על ידי המשתמש
def test_return_book():
    new_book = Book("bbb", "aaa")
    my_library.add_book(new_book)
    my_library.add_user("yaffi")
    my_library.add_user("tzipi")
    my_library.check_out_book("yaffi", my_library.books[0])
    my_library.return_book("tzipi", my_library.books[0])
    assert not my_library.books[0].is_checked_out


###בדיקה שהפונקציה תומכת בחיפושים חלקיים )חיפוש לפי חלק מהשם(
def test_search_books():
    new_book = Book("abc", "aaa")
    my_library.add_book(new_book)
    books = my_library.search_books("ab")
    assert new_book in books
