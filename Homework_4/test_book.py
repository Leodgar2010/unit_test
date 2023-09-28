import unittest
from unittest.mock import Mock

from book import BookService


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = BookService(Mock())

    def test_find_by_id(self):
        book_title = "Братья Карамазовы"
        self.service.find_by_title(book_title)
        self.service.book_repository.find_by_title.assert_called_with(book_title)