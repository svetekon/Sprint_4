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
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # попытка добавить дубликат книги
    def test_add_new_book_add_duplicate(self): 
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        
        assert len(collector.get_books_genre()) == 1

    # добавление книги с максимальным именем (40 символов)
    def test_add_new_book_add_book_with_40_characters(self):
        collector = BooksCollector()
        
        book_name = 'А' * 40
        collector.add_new_book(book_name)
        
        assert book_name in collector.get_books_genre()

    # попытка добавить книгу с именем больше 40 символов
    def test_add_new_book_add_book_with_41_characters(self):
        collector = BooksCollector()
        
        book_name = 'А' * 41
        collector.add_new_book(book_name)
        
        assert book_name not in collector.get_books_genre()

    # установка жанра из списка
    def test_set_book_genre_set_valid_genre(self):
        collector = BooksCollector()
        
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        
        assert collector.get_book_genre('1984') == 'Фантастика'


    # установка несуществующего жанра
    def test_set_book_genre_set_invalid_genre(self):
        collector = BooksCollector()
        
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Несуществующий жанр')
        
        assert collector.get_book_genre('1984') == ''

    # получение списка книг одного жанра
    def test_get_books_with_specific_genre_get_fantasy_books(self):
        collector = BooksCollector()
        
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.add_new_book('Фонд')
        
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Фонд', 'Фантастика')
        
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        
        assert 'Дюна' in fantasy_books
        assert 'Фонд' in fantasy_books
        assert 'Оно' not in fantasy_books
        assert len(fantasy_books) == 2

     # проверка, что книги с возрастным рейтингом не попадают в список детских
    def test_get_books_for_children_exclude_horror_and_detective(self):
        collector = BooksCollector()
        
        collector.add_new_book('Сказка')
        collector.add_new_book('Страшилка')
        collector.add_new_book('Детектив')
        
        collector.set_book_genre('Сказка', 'Мультфильмы')
        collector.set_book_genre('Страшилка', 'Ужасы')
        collector.set_book_genre('Детектив', 'Детективы')
        
        children_books = collector.get_books_for_children()
        
        assert 'Сказка' in children_books
        assert 'Страшилка' not in children_books
        assert 'Детектив' not in children_books

    
    #добавление книги в избранное
    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        
        assert 'Властелин колец' in collector.get_list_of_favorites_books()

    # попытка добавить книгу в избранное дважды
    def test_add_book_in_favorites_add_duplicate(self):
        collector = BooksCollector()
        
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        
        assert len(collector.get_list_of_favorites_books()) == 1

    #удаление книги из избранного
    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        collector.delete_book_from_favorites('Хоббит')
        
        assert 'Хоббит' not in collector.get_list_of_favorites_books()

    #получение пустого списка избранного
    def test_get_list_of_favorites_books_get_empty_list(self):
        collector = BooksCollector()
        
        favorites = collector.get_list_of_favorites_books()
        
        assert len(favorites) == 0
        assert favorites == []
