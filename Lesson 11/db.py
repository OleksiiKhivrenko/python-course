# Существует 3 типа отношений:
# "Один к одному"
# "Один ко многим"
# "Многое ко многим"

# атомарная форма записи

# простые и составные первичные ключи
# ключ и з одного поля
# составные ключ из 2 полей
# естественный ключ
# исскуственный код

# поиск по первичным ключам самый быстрый поиск

# 1) неключевые поля зависят от всех первичных ключей
# 2) все неключевые зависят от ключевых
# 3) все неключевые не зависят от не ключевых

# процес нормализации
# процес денормализации - все атомарно, но запрос очень большой

# foreign key внешний ключ
#
# SELECT title, genre - какие таблицы вывести
# FROM books
# INNER JOIN genres ON (genres.id = books.genre_id);
# обьеденение таблиц по условию


# Этот путь считается более правильным, чем классический:
#
# SELECT title, genre
# FROM books
# LEFT JOIN genres ON (genres.id = books.genre_id)
# WHERE genre IS NULL;


# UNION
# обьеденяет результаты запросы
# select title, genre from books right join genres using(genre_id);

# aliases
# автор название книги жанр
# авторы таблиц связей жанры книги

# select * from authors_books ab left join authors a on (ab.author_id = a.id) ;
#  author_id | book_id | id |      name       |    year
# -----------+---------+----+-----------------+------------
#          1 |       4 |  1 | Фрейк Герберт   | 1970-01-01
#          2 |       1 |  2 | Михаил Булгаков | 1970-01-01
#          3 |       3 |  3 | Джек Лондон     | 1970-01-01
#          4 |       2 |  4 | Йоган Гете      | 1970-01-01

# select * from authors_books ab left join authors a on (ab.author_id = a.id) left join books b on (ab.book_id = b.id);
# select * from authors_books ab left join authors a on (ab.author_id = a.id) left join books b on (ab.book_id =
# b.id) inner join genres g on (b.genre_id = g.id);
# select title, genre from books left join genres on (genres.genre_id = books.genre_id);

# select a.name, b.title, g.genre from authors_books ab left join authors a on (ab.author_id = a.id) left join books b on (ab.book_id = b.id) inner join genres g on (b.genre_id = g.genre_id);

# select a.name as name, b.title as book, g.genre from authors_books ab inner join authors a on (ab.author_id = a.id) inner join books b on (ab.book_id = b.id) inner join genres g on (b.genre_id = g.genre_id);

# псевдоним полезен для одной таблицы

# Index
# тригеры
# представления
# хранимые процедуры
# транзакции

# 2 селекта в телеграм

#select * from users u inner join gender g on (u.gender_id = g.ge

