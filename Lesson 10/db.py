# distinct
# select * from word;
# select distinct * from word;

# WHERE
# select distinct word from word where length(word) > 4;
# select distinct word from word where length(word) > 4 and length(word) < 7;
# select distinct word from word where length(word) between 4 and 6;
# select word, vocabulary_id from word group by 1, 2;
# select word, count(*) from word group by 1;
# select word, length(word) from word group by 1, 2;
# select word, count(*), length(word) from word group by 1;
# select word, count(*), length(word), string_agg(word, ', ') from word group by 1;
# select word, count(*), length(word), string_agg(word, ', ') from word where word != 'release' group by 1;
# select word, count(*) as num, length(word) as len, string_agg(word, ', ') from word where word != 'release' group by 1 having length(word) > 2;
# select word, count(*) as num, length(word) as len, string_agg(word, ', ') from word where word != 'release' group by 1 having length(word) > 2 order by len;
# select word, count(*) as num, length(word) as len, string_agg(word, ', ') from word where word != 'release' group by 1 having length(word) > 2 order by num desc;
# select * from word order by vocabulary_id, id desc;
# GROUP BY HAVING

# LIMIT и OFFSET

# test=# select * from word order by 3, 2 limit 3;
#  id |  word  | vocabulary_id
# ----+--------+---------------
#   1 | have   |             1
#   2 | IP     |             2
#   5 | TCP/IP |             2
# (3 rows)
#
# test=# select * from word order by 3, 2 limit 3 offset 3;
#  id |   word   | vocabulary_id
# ----+----------+---------------
#   6 | Function |             3
#   3 | Kanban   |             3
#   4 | have     |             7
# (3 rows)

#
# Максимально
# подробная
# схема
# запроса
# select
# выглядит
# так:
#
# SELECT
# < field1 >,
# < field2 >,
# < field3 >
# ...
# FROM
# < table1 >,
# < table2 >,
# < joins >,
# < views >,
# < temp_table >
# ...
# WHERE
# < cond >
#
# ORDER
# BY
# < field1 > ASC
# < field3 > DESC
# GROUP
# BY
# < field
# 1 >
# HAVING
# < cond
# with aggr function >
# LIMIT
# N, M

#  select id 4, 5 from actors;
# insert into actors (fullname, films) values('Ivan Petrov', '{Film 1, Film 2}'), ('Grisha Odin', '{Film 2, Film3, Film 4}'), ('Andrey Pyatockin', '{Film2, Film6, Film20}'), ('Oleg Ivanov', '{Film10, Film20, Film30}');
# UPDATE actors SET films = '{Film 1, Film 2, Film 3}' WHERE id IN (4, 5);

# GET ALL USERS
# \du -
# create user {user} with password '{password}';
# ALTER USER {username} WITH SUPERUSER;
