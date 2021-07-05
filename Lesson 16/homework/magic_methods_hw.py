"""
Реализуйте необходимые методы для того, чтобы следующий код выполнился

Должна быть возможность инициализировать LinkedList с помощью списка, или пустым.
"""


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Element(value)
            return

        e = self.head
        while e.next is not None:
            e = e.next
        e.next = Element(value)


ll = LinkedList()
ll2 = LinkedList([1, 2, 3])

print(ll)
# empty list should be represented as two pipes (vertical lines)
# || 

print(ll2)
# |1 -> 2 -> 3|

ll2.append('new')
print(ll2)
# |1 -> 2 -> 3 -> 'new'|

print(len(ll2))
# 4

print(ll2[2])
# 3

ll2[2] = 'changed'
print(ll2)
# |1 -> 2 -> 'changed' -> 'new'|

del ll2[1]
print(ll2)
# |1 -> 'changed' -> 'new'|

print('truthy' if ll else 'falsy')
# falsy

print('truthy' if ll2 else 'falsy')
# truthy

ll3 = LinkedList([5, 6])
print(ll2 + ll3)
# |1 -> 'changed' -> 'new' -> 5 -> 6|

ll4 = LinkedList([1, 'changed', 'new'])
print('equal' if ll2 == ll4 else 'not equal')
# equal

print('not equal' if ll2 != ll3 else 'equal')
# not equal

# Если предыдущего покажется маловато, то вот со звездочкой на десерт:
# for i in ll2:
#     print(i)
