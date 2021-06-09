class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employee(Human):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_paid(self):
        return self.salary


class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, language, bonus):
        super().__init__(first_name, last_name, salary)
        self.language = language
        self.bonus = bonus

    def get_paid(self):
        return super().get_paid() + self.bonus


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, coefficient):
        super().__init__(first_name, last_name, salary)
        self.coefficient = coefficient

    def get_paid(self):
        return super().get_paid() * self.coefficient


employees = [Programmer('Anton', 'Martynov', 1000, 'python', 100),
             Manager('Kyrylo', 'Kozhemyaka', 2000, 1.2),
             Employee('Sam', 'Smith', 800)]

for e in employees:
    print(f"{e} have to be paid: {e.get_paid()}")
