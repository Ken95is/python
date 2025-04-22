'=======================================OOP======================================='
# OOP - Object-orientated programming
# ООП - Обьектно ориентированное программирование(парадигма)

# class - это шаблон
# object(instance, экземпляр) - это конечный продукт класса

class Person:
    # переменные внутри класса (обьекта) - аттрибуты
    arms = 2
    legs = 2
    
    def __init__(self, name, age, prof):
        # __init__ - метод, который будет добавлять в обьект те аттрибуты, которые у всех обьектов разные 
        # self - ссылка на обьект, который только что создался 
        self.name = name
        self.age = age
        self.prof = prof

    # Функции внутри класса (обьекта) - методы
    def walk(self):
        print(f'{self.name}, ходить')

    def swim(self):
        print(f'{self.name} плавать')

obj1 = Person('katana', 21, 'dev')
obj2 = Person('Nick', 21, 'dev')
obj3 = Person('Laura', 20, 'senior dev')

obj1.walk()
obj1.swim()
obj2.swim()

print(obj1.arms)
print(obj1.name)
print(obj3.name)
print(obj2.age)

print(obj2.legs)




class Calc:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b
    

calc = Calc()
print(calc.add(4, 5))
print(calc.sub(10, 5))
print(calc.div(4, 5))
print(calc.mult(10, 5))
