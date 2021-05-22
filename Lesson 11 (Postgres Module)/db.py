# Задача 1:
#
# Создать таблицу, выдающую следующее:
#
# select * from users;
#
# 1 | m      | Vasya  | mmm@mail.com
# 2 | m      | Alex   | mmm@gmail.com
# 3 | m      | Alexey | alexey@gmail.com
# 4 | f      | Helen  | hell@gmail.com
# 5 | f      | Jenny  | eachup@gmail.com
# 6 | f      | Lora   | tpicks@gmail.com
#
# Задача 2:
#
# Получить результат вида:
#
# We have 3 boys!
# We have 3 girls!
#
# Задача 3:
#
# Получить результат вида:
#
# This is Vasya, he has email mmm@mail.com
# This is Alex, he has email mmm@gmail.com
# This is Alexey, he has email alexey@gmail.com
# This is Helen, she has email hell@gmail.com
# This is Jenny, she has email eachup@gmail.com
# This is Lora, she has email tpicks@gmail.com

# create table gender(id serial primary key, gender varchar(1), gender_id integer)
# insert into gender(gender, gender_id) values ('m', 0), ('f', 1);

# create users(id serial primary key, name varchar(255));
# insert into
# users(name)
# values('Vasya'), ('Alex'), ('Alexey'), ('Helen'), ('Jenny'), ('Lora');

# create table email(id serial primary key, email varchar(255), user_id integer references user(id));
# insert into email(email, user_id) values ('mmm@mail.com', 1), ('mmm@gmail.com', 2), ('alexey@gmail.com', 3), ('hell@gmail.com', 4), ('eachup@gmail.com'
# , 5), ('tpicks@gmail.com', 6);
# \dt
#
# ALTER TABLE table_name
# ADD COLUMN new_column_name data_type constraint;
#  alter table users add column gender_id integer;

# insert into users(name, gender_id) values('Vasya', 0), ('Alex', 0), ('Alexey', 0), ('Helen', 1), ('Jenny', 1), ('Lora', 1);

# select u.user_id, g.gender, u.name, e.email from users u inner join gender g on (u.gender_id = g.gender_id) inner join email e on (e.user_id = u.user_id) order by user_id asc;

# select
# case
# when
# g.gender_id = 0
# then
# 'We have ' | | count(*) | | ' boys!'
# end
# from users u
#
# inner
# join
# gender
# g
# on(u.gender_id = g.gender_id) inner
# join
# email
# e
# on(e.user_id = u.user_id) group
# by
# g.gender_id
# having
# count(*) > 1;
# select case when g.gender_id=0 then 'We have ' || count(*) || ' boys!' when g.gender_id=1 then 'We have ' || count(*) || ' girls!' end from users u inner join gender g on (u.gender_id = g.gender_id) inner join email e on (e.user_id = u.user_id) group by g.gender_id having count(*) > 1;
#  select case when u.name is not null then 'This is ' || u.name || ', he has email ' || e.email end from users u inner join gender g on (u.gender_id = g.gender_id) inner join email e on (e.user_id = u.user_id) order by u.user_id;


# select case when g.gender_id=0 then 'We have ' || count(*) || ' boys!' when g.gender_id=1 then 'We have ' || count(*) || ' girls!' end from users u inner join gender g on (u.gender_id = g.gender_id) inner join email e on (e.user_id = u.user_id) group by g.gender_id having count(*) > 1;

# select case when gender='m' then 'We have ' || count(*) || ' boys!' when gender='f' then 'We have ' || count(*) || ' girls!' end from users group by gender having count(*) >= 0;
# select case when name is not null then 'This is ' || name || ', he has email ' || email end from users;


