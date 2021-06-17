class Base:
    def __init__(self):
        self.test = 'test'
        self.__kind = 'Parent'

    def who_am_i(self):
        return self.__kind


class Child(Base):
    def __init__(self):
        super(Child, self).__init__()

    def get_parent_kind(self):
        return self.who_am_i()


c = Child()
c.who_am_i()

print(dir(c))
print(c.get_parent_kind())
