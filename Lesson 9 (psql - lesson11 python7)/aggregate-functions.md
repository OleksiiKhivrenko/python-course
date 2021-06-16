# Avg
Находит среднее значение. Входной параметр должен представлять один из следующих типов: smallint, int, bigint, real, 
double precision, numeric, interval. Для целочисленнных параметров результатом будет значение типа numeric, для параметров, которые представляют число с плавающей точкой, - значение типа double precision.
```SELECT AVG(Price) AS Average_Price FROM Products;```
```SELECT AVG(Price) FROM Products WHERE Company='Apple';```
```SELECT AVG(Price * ProductCount) FROM Products```


# Count
Функция **Count** вычисляет количество строк в выборке. Есть две формы этой функции. Первая форма COUNT(*) подсчитывает 
число строк в выборке:
```SELECT COUNT(*) FROM Products;```
```SELECT COUNT(DISTINCT Company) FROM Products;```


# Min и Max
Функции **Min** и **Max** возвращают соответственно минимальное и максимальное значение по столбцу. Например, найдем 
минимальную цену среди товаров:
```SELECT MIN(Price) FROM Products;```
```SELECT MAX(Price) FROM Products;```


# Sum
Функция Sum вычисляет сумму значений столбца. Например, подсчитаем общее количество товаров:
```SELECT SUM(ProductCount) FROM Products;```
```SELECT SUM(ProductCount * Price) FROM Products;```


# BOOL_AND и BOOL_OR
возвращает true, если хотя бы одно значение в наборе равно true:
```SELECT BOOL_OR(IsDiscounted) FROM Products;```

возвращает true, если все значения в наборе равны true:
```SELECT BOOL_AND(IsDiscounted) FROM Products;```


# STRING_AGG
Функция STRING_AGG() объединяет набор строковых значений или значений bytea. Например, выберем названия всех товаров:
```
SELECT STRING_AGG(DISTINCT Company, ', ') FROM Products;
 
-- результат операции
-- Apple, HMD Global, HTC, Samsung 
```
