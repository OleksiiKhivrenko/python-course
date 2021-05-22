# тип данных - диапазон значений при определенных правилах, допустимое множество значений

# psql -U {{ user }} -d {{ dbname }} -h {{ host }}
# -U {{ user }} - подключение через пользователя
# -d {{ dbname }} - подключение к дб
# -h {{ host }} - подключение к хосту
# https://www.postgresqltutorial.com/psql-commands/
# create database {{dbname}};
# drop database {{dbname}};
# \c pypy - switch to another db
# psql -l, \q - display db's
# \d - show all relations (tables) describe

# CRUD - create, read, update, delete

# C - create
# create table students (id serial, fullname varchar not null default 'Noname');

# R (read)
# \d students
# \dt

# множество значений и операций над этими значениями
# postgres строго статически типизирован
# числовые - отличаются диапазоном и размером
# 00110101 - 2*(pow5) + 2*(pow4) + 2(pow2) + 2(pow0)
# -32767 to 32768 -2*(pow15) to 2(pow15) - 2byte
# varchar
# картинка

# macadr - datatype
# sqlite
# alter - изменение alteration - U (update)
# field definition
# https://www.postgresqltutorial.com/postgresql-alter-table/


# https://postgrespro.ru/docs/postgresql/9.6/ddl-alter
# ALTER TABLE products ALTER COLUMN product_no DROP NOT NULL;
# ALTER TABLE products ALTER COLUMN price SET DEFAULT 7.77;
# ALTER TABLE products ALTER COLUMN price DROP DEFAULT;
# ALTER TABLE actors ALTER COLUMN fullname TYPE varchar(30);
# ALTER TABLE films DROP films;


