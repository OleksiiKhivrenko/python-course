class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"The object Element - {self.value}"

    def __str__(self):
        return f"Element - {self.value}"


el = Element([1, 2, 3])
print(el)
