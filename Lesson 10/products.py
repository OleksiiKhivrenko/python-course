# create table customer(
# id serial primary key,
# name varchar(255),
# phone varchar(30),
# email varchar(255)
# )
# ;
# Indexes
# customer_pkey - link to uniq key

# create table product(
# id serial primary key,
# name varchar(255),
# description text,
# price integer)
# ;
#

#  create table product_photo(
#  id serial primary key,
#  url varchar(255),
#  product_id integer references product(id)
#  );

# create table cart(
# customer_id integer references customer(id),
# id serial primary key);


# JOIN
# select * from product_photo pp;
# select pp.* from product_photo pp;
# select pp.* from product_photo pp left join product p on p.id=pp.product_id;

# inner join - те записи которые существуют в обоих табличках
# left join - записи, которые есть в левой табличке, дополняются правой табличкой или нулами если нет совпадение
# right join - наоборот

# select * from product_photo cross join product;
# select * from product_photo as pp inner join product as p on pp.product_id=p.id;
# selects name, description, price, product_id as id from product_photo as pp left join product p on pp.product_id=p.id;
# select  name, description, price, url, p.id from product_photo as pp right join product p on pp.product_id=p.id;
#  update product_photo set url='iphone_image_1' where id=1;
# insert into product_photo (url, product_id) values ('apple_watch_img', 2);
# select  name, description, price, url, p.id fbbfrom product p left join product_photo pp on pp.product_id=p.id;

# insert into cart (customer_id) values (1);
# insert into cart_product (cart_id, product_id) values (1, 1), (1, 2);
# select c.name, cart.id as cart_id, cp.product_id, p.price from customer c left join cart on cart.customer_id=c.id left join customers_products_cart cp on cp.cart_id=cart.id left join product p on p.id = cp.product_id;

# sum and group and products
# select c.name, sum(p.price) from customer c left join cart on cart.customer_id=c.id left join customers_products_cart cp on cp.cart_id=cart.id left join product p on p.id = cp.product_id group by c.name;
# select c.name, coalesce(sum(p.price), 0) from customer c left join cart on cart.customer_id=c.id left join customers_products_cart cp on cp.cart_id=cart.id left join product p on p.id = cp.product_id group by c.name;
# coalesce - coalesce(sum(p.price), 0) - replace null with value

# select c.name, coalesce(sum(p.price), 0) as orders_sum from customer c left join cart on cart.customer_id=c.id left join customers_products_cart cp on cp.cart_id=cart.id left join product p on p.id = cp.product_id group by c.name order by orders_sum desc;
# select c.name, coalesce(sum(p.price), 0) as orders_sum from customer c left join cart on cart.customer_id=c.id left join customers_products_cart cp on cp.cart_id=cart.id left join product p on p.id = cp.product_id group by c.name having sum(p.price)>0;

# Отличие WHERE от HAVING - having фильтрует группы (по агрегирующим групам sum count)
# having фильтрует сгрупированные значения group by

# select * from customer order by name using ~ < ~;

# LIMIT
# select * from customer order by name using ~<~ limit 2;
# возвращает определенное значение
# limit 1 offset 1 - используется для пагинации
