'==================================Полиморфизм=================================='
# полиморфизм - принцип ООП, в котором в разных классах методы называются одинаково, но реализация разная (один интерфейс - разный функционал)

class Dog:
    def voice(self):
        print('Гав-гав')

class Cat:
    def voice(self):
        print('Мяу-мяу')

class Duck:
    def voice(self):
        print('Кря-кря')

objects = [Dog(), Cat(), Duck(), Cat()]
for obj in objects:
    obj.voice()

