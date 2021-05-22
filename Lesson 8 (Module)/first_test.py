def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    # return ['bulochka' for i in range(number+1)]
    return "".join(['bulochka' for _ in range(number)])


def my_sum(list_of_numbers):
    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list_of_numbers:

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    
    """
    pass
    #  ...wite your code here
    total = 0
    for num in list_of_numbers:
        total += num

    return total


def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    pass
    #  ...wite your code here
    return " ".join(map(lambda word: word[:6] + "*" if len(word) > 6 else word, string.split()))


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    pass
    #  ...wite your code here
    strs = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            strs.append(word)
    return len(strs)
