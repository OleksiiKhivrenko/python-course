# mixins - необходимы для избежания переопределения кода
# множественное наследование

class RadioMixin:
    def play(self, track):
        print(f"Now is playing {track}")


class Car(RadioMixin):
    pass


class Smartphone(RadioMixin):
    pass


c = Car()
c.play("Bohemian")

s = Smartphone()
s.play("Something")
