# qa_python
## Тестирование приложения BooksCollector

Этот проект представляет собой тестирование приложения **BooksCollector**, которое управляет книгами, их жанрами и избранными книгами.

Приложение позволяет:
- Добавлять книги в коллекцию.
- Устанавливать жанры книг.
- Получать информацию о жанре книги.
- Получать список книг по жанрам.
- Управлять избранными книгами.

### Покрытые тесты:

1. **test_add_new_book_adds_book_without_genre**  
   Проверяет, что метод `add_new_book` добавляет книгу в коллекцию без указания жанра. Книга добавляется в словарь `books_genre` с пустым значением для жанра.

2. **test_set_book_genre_sets_correct_genre**  
   Проверяет, что метод `set_book_genre` корректно устанавливает жанр книги, если книга существует в коллекции и жанр входит в список доступных жанров.

3. **test_get_book_genre_returns_genre**  
   Проверяет, что метод `get_book_genre` возвращает правильный жанр книги по её названию.

4. **test_get_books_with_specific_genre_returns_correct_books**  
   Проверяет, что метод `get_books_with_specific_genre` возвращает только книги с заданным жанром из коллекции.

5. **test_get_books_genre_returns_all_books**  
   Проверяет, что метод `get_books_genre` возвращает все книги, добавленные в коллекцию, с указанными жанрами.

6. **test_get_books_for_children_filters_out_age_rating_books**  
   Проверяет, что метод `get_books_for_children` корректно фильтрует книги, исключая те, которые имеют возрастной рейтинг (указаны в `genre_age_rating`).

7. **test_add_book_in_favorites_adds_book**  
   Проверяет, что метод `add_book_in_favorites` добавляет книгу в список избранных, если книга существует в коллекции и еще не была добавлена в избранное.

8. **test_delete_book_from_favorites_removes_book**  
   Проверяет, что метод `delete_book_from_favorites` удаляет книгу из списка избранных, если она там присутствует.

9. **test_get_list_of_favorites_books_returns_correct_list**  
   Проверяет, что метод `get_list_of_favorites_books` возвращает правильный список избранных книг.


