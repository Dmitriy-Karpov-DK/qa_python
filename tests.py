import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Закат')

        assert 'Закат' in collector.books_genre

    def test_add_new_book_add_book_with_name_more_40_char(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить, но мышь против')

        assert 'Что делать, если ваш кот хочет вас убить, но мышь против' not in collector.books_genre

    def test_set_book_genre_set_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Закат')
        collector.set_book_genre('Закат', 'Фантастика')

        assert 'Фантастика' == collector.books_genre['Закат']

    def test_get_book_genre_show_book_genre_by_name(self):
        collector = BooksCollector()

        collector.add_new_book('Закат')
        collector.set_book_genre('Закат', 'Фантастика')

        assert 'Фантастика' == collector.get_book_genre('Закат')

    def test_get_books_with_specific_genre_show_four_books_by_genre(self):
        collector = BooksCollector()

        books = ['Закат', 'Рассвет', 'День', 'Ночь']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Фантастика')

        assert books == collector.get_books_with_specific_genre('Фантастика')

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Закат', 'Фантастика'],
            ['Рассвет', 'Фантастика'],
            ['Пуаро', 'Детективы'],
            ['Шерлок Холмс', 'Детективы']
        ]
    )
    def test_get_books_genre_show_current_dict(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre == collector.get_books_genre()

    def test_get_books_for_children_show_two_books_out_of_four(self):
        collector = BooksCollector()

        books1 = ['Закат', 'Рассвет']
        for book in books1:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Фантастика')

        books2 = ['Пуаро', 'Шерлок Холмс']
        for book in books2:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Детективы')

        assert books1 == collector.get_books_for_children()

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Закат')
        collector.set_book_genre('Закат', 'Фантастика')
        collector.add_book_in_favorites('Закат')

        assert 'Закат' in collector.favorites

    def test_add_book_in_favorites_re_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Закат')
        collector.set_book_genre('Закат', 'Фантастика')
        collector.add_book_in_favorites('Закат')
        collector.add_book_in_favorites('Закат')

        assert 1 == len(collector.favorites)

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Закат')
        collector.set_book_genre('Закат', 'Фантастика')
        collector.add_book_in_favorites('Закат')
        collector.delete_book_from_favorites('Закат')

        assert 0 == len(collector.favorites)

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Закат', 'Фантастика'],
            ['Рассвет', 'Фантастика'],
            ['Пуаро', 'Детективы'],
            ['Шерлок Холмс', 'Детективы']
        ]
    )
    def test_get_list_of_favorites_books_show_list_favorites(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert collector.favorites == collector.get_list_of_favorites_books()
