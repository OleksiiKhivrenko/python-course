class Week {
    constructor() {
        this.dates = {
            ru: ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
            en: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Monday']
        }
    }
    getNameOdDay(lng, day) {
        return this.dates[lng][day]
    }
}

const week = new Week('ru', 0)

console.log(week.getNameOdDay())
