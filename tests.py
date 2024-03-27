from main import BooksCollector
import pytest
class TestBooksCollector:
    # проверка добавления двух книг в словарь ==============================
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_1')
        collector.add_new_book('Книга_2')
        assert len(collector.get_books_genre()) == 2

    # проверка присвоения допустимых жанров для книги из списка ==========================
    @pytest.mark.parametrize('genre',['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_for_book_in_list(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга_3')
        collector.set_book_genre('Книга_3',genre)
        assert collector.get_book_genre('Книга_3') == genre

    # проверяем что жанр, который отсутствует в списке не буден присвоен ======================
    def test_set_book_ganre_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_4')
        collector.set_book_genre('Книга_4', 'Другое')
        assert collector.get_book_genre('Книга_4') == ''


    # проверка вывода списка книг с определённым жанром   ========================
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_5')
        collector.set_book_genre('Книга_5', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Книга_5']

    #