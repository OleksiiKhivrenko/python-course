/** 1.
 * Создать цикл на 10 итераций. На каждой итерации если i четное, то вывести в консоль слово Fiz, если i не
 * четное, то вывести в консоль слово Buz,если i кратное цифре 3, то вывести FizBuz.
 */

function fizzBuzz() {
    for (let i = 1; i <= 10; i++) {
        if (!(i % 3)) {
            console.log("FizBuz");
        } else if (!(i % 2)) {
            console.log("Fiz");
        } else if (i % 2) {
            console.log("Buz");
        }
    }
}

fizzBuzz();

/** 2.
 * Написать логику нахождения факториала числа 10.
 */

function fact(num) {
    let counter = 0;
    let values = [];

    if (num === 0 || num === 1) {
        return 1;
    } else if (num < 0) {
        throw new Error("Please use positive value or 0");
    } else {
        for (let i = 1; i <= num; i++) {
            values.unshift(i);
            counter++;
        }
        return values.reduce((val, acc) => val * acc, 1);
    }
}

console.log(fact(15));

/**
 * В пачке бумаги 500 листов. За неделю в офисе расходуется 1200 листов.
 * Какое наименьшее количество пачек бумаги нужно
 * купить в офис на 8 недель?
 * Запрещавется использовать какое-либо округление (Math.ceil, Math.floor, ~~, parseInt).
 */

function calculateNumberOfPapersPack(weeks = 1) {
    if (weeks < 0) {
        throw new Error("Please use positive number of weeks");
    }

    const sheetsInReamPaper = 500;
    const consumptionPerWeek = 1200;
    const notRoundedNumber = consumptionPerWeek / sheetsInReamPaper * weeks;

    if (!(notRoundedNumber % 1)) {
        return notRoundedNumber;
    } else {
        const str = notRoundedNumber.toString().split(".")[0];
        return +str + 1;
    }
}

console.log(calculateNumberOfPapersPack(2));
console.log(calculateNumberOfPapersPack(8));

/**
 * Создать функцию, которая выведет в консоль номер этажа и номер подъезда по номеру квартиры.
 * Этажей у нас 9, квартир на этаже по 3
 * Запрещавется использовать какое-либо округление (Math.ceil, Math.floor, ~~, parseInt).
 */

function getNumberOfFloorAndApartments(apartmentsNumber) {
    const numberOfFloors = 9;
    const numberOfApartments = 3;
    const numberOfApInHome = numberOfFloors * numberOfApartments;

    if (apartmentsNumber < 1 || apartmentsNumber > numberOfApInHome) {
        throw new Error("This apartment is not in the home.")
    } else {
        const home = [];

        for (let i = 0; i < numberOfFloors; i++) {
            const floor = [];

            for (let j = 1; j <= numberOfApartments; j++) {
                floor.push(i * numberOfApartments + j);
            }

            home.push(floor);
        }

        return home.findIndex(i => i.includes(apartmentsNumber)) + 1;
    }
}

console.log("Floor: ", getNumberOfFloorAndApartments(10));

/**
 * Вывести в консоль пирамиду. Переменная указывает количество строк из которых построится пирамида.
 * Пирамида должна строится в одинаковом визуально виде между собой, но строго учитывая кол-во строк
 * const medianNumber = 8
 -------#-------  //1
 ------###------  //2
 -----#####-----  //3
 ----#######----  //4
 ---#########--   //5
 --###########--  //6
 -#############-  //7
 ###############  //8
 */

function createPyramid(num = 8) {
    const pyramid = [];
    const pyramidStrokeLength = num * 2 - 1;

    for (let i = num; i > 0; i--) {
        const step = num - i;
        const level = Array(pyramidStrokeLength)
            .fill('#')
            .map((item, index, arr) => index < step || arr.length - step <= index ? '_' : item)
            .join("");
        pyramid.unshift(level);
    }

    return pyramid.join("\n")
}

console.log(createPyramid(9))




