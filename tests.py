from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_adds_book_without_genre(self):
        collector = BooksCollector()

            # Добавляем книгу без жанра
        collector.add_new_book('Гарри Поттер')

            # Проверяем, что книга добавлена и у неё пустой жанр
        assert 'Гарри Поттер' in collector.get_books_genre()
        assert collector.get_books_genre()['Гарри Поттер'] == ''

        # Тест на установку жанра книги
    def test_set_book_genre_sets_correct_genre(self):
        collector = BooksCollector()

            # Добавляем книгу без жанра
        collector.add_new_book('Гарри Поттер')

            # Устанавливаем жанр
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

            # Проверяем, что жанр установлен правильно
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

        # Тест на получение жанра книги
    def test_get_book_genre_returns_genre(self):
        collector = BooksCollector()

            # Добавляем книгу без жанра
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

            # Получаем жанр книги
        genre = collector.get_book_genre('Гарри Поттер')

            # Проверяем, что жанр вернулся правильно
        assert genre == 'Фантастика'

        # Тест на получение книг с конкретным жанром
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()

            # Добавляем книги с разными жанрами
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')

            # Получаем книги с жанром 'Фантастика'
        books = collector.get_books_with_specific_genre('Фантастика')

            # Проверяем, что книга "Гарри Поттер" есть в списке
        assert 'Гарри Поттер' in books

            # Проверяем, что книга "Шрек" не в списке
        assert 'Шрек' not in books

        # Тест на получение всех книг
    def test_get_books_genre_returns_all_books(self):
        collector = BooksCollector()

            # Добавляем книги
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шрек')

            # Получаем все книги
        books = collector.get_books_genre()

            # Проверяем, что количество книг равно 2
        assert len(books) == 2

            # Проверяем, что обе книги есть в словаре
        assert 'Гарри Поттер' in books
        assert 'Шрек' in books

        # Тест на получение книг для детей (без возрастного рейтинга)
    def test_get_books_for_children_filters_out_age_rating_books(self):
        collector = BooksCollector()

            # Добавляем книги с жанром, подходящим детям и с возрастным рейтингом
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')

            # Получаем книги для детей
        children_books = collector.get_books_for_children()

            # Проверяем, что "Шрек" есть в списке для детей
        assert 'Шрек' in children_books

            # Проверяем, что "Оно" нет в списке для детей (оно не подходит по возрастному рейтингу)
        assert 'Оно' not in children_books

        # Тест на добавление книги в избранное
    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()

            # Добавляем книгу и добавляем её в избранное
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

            # Проверяем, что книга есть в списке избранных
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

        # Тест на удаление книги из избранного
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()

            # Добавляем книгу и добавляем её в избранное
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

            # Удаляем книгу из избранного
        collector.delete_book_from_favorites('Гарри Поттер')

            # Проверяем, что книга больше не в избранных
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

        # Тест на получение списка избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()

            # Добавляем книги и добавляем одну в избранное
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Гарри Поттер')

            # Получаем список избранных книг
        favorites = collector.get_list_of_favorites_books()

            # Проверяем, что "Гарри Поттер" есть в списке избранных
        assert 'Гарри Поттер' in favorites

            # Проверяем, что "Шрек" не в избранных
        assert 'Шрек' not in favorites