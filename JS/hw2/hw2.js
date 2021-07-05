/**
 * Дан объект с городами и странами.
 * Вывести масив значения в котором будут строки преобразованные в данный формат: <Столица> - это <Страна>.
 const citiesAndCountries = {
        'Киев': 'Украина',
        'Нью-Йорк': 'США',
        'Амстердам': 'Нидерланды',
        'Берлин': 'Германия',
        'Париж': 'Франция',
        'Лиссабон': 'Португалия',
        'Вена': 'Австрия',
    };

 const result = ['Киев - это Украина', 'Нью-Йорк - это США', ... и т.д.]
 */

function getFormattedArrayByCountriesObj() {
    const citiesAndCountries = {
        "Киев": 'Украина',
        'Нью-Йорк': 'США',
        'Амстердам': 'Нидерланды',
        'Берлин': 'Германия',
        'Париж': 'Франция',
        'Лиссабон': 'Португалия',
        'Вена': 'Австрия',
    };

    return Object.keys(citiesAndCountries).map(item => `${item} - это ${citiesAndCountries[item]}`);
}

console.log(getFormattedArrayByCountriesObj())

/**
 * Создать функцию которая выведет многомерный массив A.
 * Данный массив содержит в себе список других массивов B.
 * Массивы B должны содержать по 3 значения.
 * Максимальное значение (в примере это переменная amount) должно делится на 3 нацело.
 *
    // Вариант 1
    function getArray(){
        const amount = 9;
        ... Your code
    }

    getArray() // выведет в консоль [ [1,2,3], [4,5,6], [7,8,9] ].


    // Вариант 2
    function getArray(){
        const amount = 12;
        ... Your code
    }

    getArray() // выведет в консоль [ [1,2,3], [4,5,6], [7,8,9], [10,11,12] ]
 */

function getArray(amount = 9) {
    if (amount < 1) {
        return [];
    }

    const lengthOfArr = 3;
    const arr = Array(Math.ceil(amount / lengthOfArr));

    for (let i = 0; i < arr.length; i++) {
        const lineValues = [];

        for (let j = 1; j <= lengthOfArr; j++) {
            if (lengthOfArr * i + j <= amount) {
                lineValues.push(lengthOfArr * i + j);
            } else {
                break;
            }
        }

        arr[i] = lineValues;
    }

    return arr;
}

console.log(getArray(13))

/**
 * Cоздать объект с названиями дней недели.
 * Где ключами будут ru и en, a значением свойства ru будет массив с
 * названиями дней недели на русском, а en - на английском.
 * После написать функцию которая будет выводить в консоль название дня недели
 * пользуясь выше созданным объектом.
 * Все дни недели начинаются с 1 и заканичаются цифрой 7
 * (1- понедельник, 7 - воскресенье). Функция хранит
 * переменную lang - название языка дня недели и переменную day - число дня недели.

    const namesOfDays = {
        ru: ['Понедельник', 'Вторник', 'Среда', ... , 'Воскресенье'],
        en: ['Monday', 'Tuesday', 'Wednesday', ... , 'Sunday'],
    }

    ------------------------------------------------

    // Пример 1

    function getNameOfDay(){
        const lang = 'en';
        const day = 7;

        ... Your code
    }

    getNameOfDay() /// 'Sunday'

    ------------------------------------------------

    // Пример 2

    function getNameOfDay(){
        const lang = 'ru';
        const day = 3;

        ... Your code
    }

    getNameOfDay() /// 'Среда'
 */

function getNameOfDay(lang, day) {
    const namesOfDays = {
        ru: ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота' , 'Воскресенье'],
        en: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' , 'Sunday'],
    }

    return namesOfDays?.[lang]?.[day]
}

console.log(getNameOfDay('ru', 3))

/**
 * Создайте функцию, которая возвращает сумму двух наименьших
 * положительных чисел из массива минимум 4 положительных целых чисел.
 * Не передаются числа с плавающей запятой или неположительные целые числа.
 * В массиве не могут содержаться одинаковые числа.
 * [19, 5, 42, 2, 77], вывод должен быть 7
 */

function getSumOfTwoMinNumbers(arr) {
    if (!(Array.isArray(arr))) {
        throw new Error("Please input array with numbers")
    } else {
        return arr.sort((a, b) => a - b).slice(0, 2).reduce((num, acc) => acc + num, 0)
    }
}

console.log(getSumOfTwoMinNumbers([19, 5, 42, 2, 77]))

/**
 * Дан массив единиц и нулей, преобразуйте эквивалентное двоичное
 * значение в целое число.
 * Например: [0, 0, 0, 1] рассматривается как 0001двоичное представление 1.
    Testing: [1, 0, 0, 0, 1] ==> 17
    Testing: [1, 0, 0, 1, 0] ==> 18
    Testing: [1, 0, 1, 0, 1] ==> 21
    Testing: [1, 1, 1, 0, 0, 1] ==> 57
 */

function getBinaryNumberFromArr(arr) {
    return parseInt(arr.join(""), 2)
}

console.log(getBinaryNumberFromArr([1, 1, 1, 0, 0, 1]))






