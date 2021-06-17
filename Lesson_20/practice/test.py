import unittest

from payments import Human, Employee, Programmer, Manager


class TestHuman(unittest.TestCase):
    def setUp(self):
        self.h = Human('John', 'Doe')

    def test_str(self):
        self.assertEqual(str(self.h), 'John Doe')


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.salary = 1000
        self.e = Employee('John', 'Doe', self.salary)

    def test_get_paid(self):
        e_get_paid_result = self.e.get_paid()
        self.assertEqual(e_get_paid_result, self.salary)


class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.test_bonus = 1000
        self.salary = 1000
        self.p = Programmer('John', 'Doe', self.salary, 'python', self.test_bonus)

    def test_get_paid(self):
        self.assertEqual(self.p.get_paid(), self.test_bonus + self.salary)


class TestManager(unittest.TestCase):
    def setUp(self):
        self.coefficient = 1.5
        self.salary = 1000
        self.p = Manager('John', 'Doe', self.salary, self.coefficient)

    def test_get_paid(self):
        self.assertEqual(self.p.get_paid(), self.salary * self.coefficient)


if __name__ == '__main__':
    unittest.main()
