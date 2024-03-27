from main import BooksCollector
import pytest
class TestBooksCollector:
    # проверка добавления двух книг в словарь ==============================
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_1')
        collector.add_new_book('Книга_2')
        assert len(collector.get_books_genre()) == 2

    # проверка добавления двух одинаковых книг в словарь ==============================
    def test_add_new_book_add_two_copy_books(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Горе от ума')
        assert len(collector.get_books_genre()) == 1

    # проверка добавления книги с длинной имени больше 40 символов  ===================
    def test_add_new_book_add_book_with_name_50_symbol(self):
        collector = BooksCollector()
        collector.add_new_book('Long_Name_Long_Name_Long_Name_Long_Name_Long_Name_')
        assert len(collector.get_books_genre()) == 0

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

    # проверка добавления двух книг в избранное  ========================================
    def test_add_book_in_favorites_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_6')
        collector.add_new_book('Книга_7')
        collector.add_book_in_favorites('Книга_6')
        collector.add_book_in_favorites('Книга_7')
        assert len(collector.get_list_of_favorites_books()) == 2

    # проверяем добавление книги в избранное, которой нет в словаре ================
    def test_add_book_in_favorites_not_in_list(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Книга_8')
        assert len(collector.get_list_of_favorites_books()) == 0

    # проверка удаления книги из избранного, если она там есть ====================
    def test_delete_book_from_favorites_if_book_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_9')
        collector.add_book_in_favorites('Книга_9')
        collector.delete_book_from_favorites('Книга_9')
        assert len(collector.get_list_of_favorites_books()) == 0

