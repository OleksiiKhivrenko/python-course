t = (1, 2, 3, 4, 5)

(x, *_, y) = t

print(x, y)
l = [1, 2, 1, 1, 1, 1, "a", "b"]

# .count - returns numbers of matched el [1, 1, 1, 1].count(1) => 4
print(l.count(1))

# set возвращает уникальные элементы
s = {1, 1, 1, 'a', 'a', 2, 5, 4}
print(s)

# import json json.dumps() json.loads() => работа с JSON данными

# a.update(dict(a=20, b=30))
# for i in a: print(a
# dict.get()
# .items() - dict items, not tuple
# .keys({"a": 1}) - dict_keys(['a'])
# .values({"a": 1}) - dict_keys([1])
