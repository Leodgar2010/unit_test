# У вас есть класс BookService, который использует интерфейс BookRepository
# для получения информации о книгах из базы данных. Ваша задача написать
# unit-тесты для BookService, используя Mockito для создания мок-объекта BookRepository.



from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str

class BookRepository (Book):
    def __init__(self, books: list[Book] = None):
        self._books = books
        if books is None:
            self._books = []

    def find_by_title(self, book_title: str) -> Book:
        return [*filter(lambda x: x.title == book_title, self._books)][0]



class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    @property
    def book_repository(self):
        return self._book_repository

    def find_by_title(self, book_title: str) -> Book:
        return self._book_repository.find_by_title(book_title)

