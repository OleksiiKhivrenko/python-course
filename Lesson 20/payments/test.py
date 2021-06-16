import unittest

from payments import Human, Employee


class HumanTest(unittest.TestCase):
    def setUp(self):
        self.h = Human('John', 'Doe')

    def test_str(self):
        self.assertEqual(str(self.h), 'John Doe')


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.e = Employee('John', 'Doe', 20001)

    def test_get_paid(self):
        e_get_paid_result = self.e.get_paid()
        self.assertEqual(e_get_paid_result, 20001)


if __name__ == '__main__':
    unittest.main()
