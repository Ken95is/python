from abc import ABC , abstractmethod, abstractproperty

# class Transport(ABC):
#     @property
#     @abstractmethod

#     def move(self):
#         ...

# class Car(Transport):
#     def move(self):
#         return 'Car is moving on the road'

# class Plane(Transport):
#     def move(self):
#         print('Plane is flying in the sky')

# obj1 = Car()
# obj2 = Plane()
# print(obj1.move())
# print(obj2.move())

'-------------------------------------------------------------'

class PaymentMethod(ABC):
    @property
    @abstractmethod

    def pay(self, amount):
        ...

class CreditCard(PaymentMethod):
    def pay(self,amount):
        self.amount = amount
        return f'Оплата {amount} через Credit Card'
    
class Paypal(PaymentMethod):
    def pay(self,amount):
        self.amount = amount
        return f'Оплата {amount} через Paypal'
    
cc = CreditCard()
pp = Paypal()
print(cc.pay(1000))
print(pp.pay(500))

'-------------------------------------------------------'

class Shape(ABC):
    def area(self):
        ...

class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        ar = self.radius ** 2 * 3.14
        return f'Площадь круга: {ar}'
    
class Rectangle(Shape):
    def area(self, a, b):
        self.a = a
        self.b = b
        ar = a * b
        return f'Площадь прямоугольника: {ar}'

cir = Circle()
rec = Rectangle()
print(cir.area(5))
print(rec.area(20, 10))
'-----------------------------------------------------'

class OutputDevice(ABC):
    m = '[Monitor] '
    p = '[Printer] '
    h = 'Hello, world!'
    def display(self):
        ...

class Monitor(OutputDevice):
    def display(self):

        return super().m + super().h
    
class Printer(OutputDevice):
    def display(self):

        return super().p + super().h
    
mon = Monitor()
pri = Printer()
print(mon.display())
print(pri.display())

'--------------------------------------------------------'

class Animal(ABC):
    def make_sound(self):
        ...

class Dog(Animal):
    def make_sound(self):
        print('Гав!')

class Cat(Animal):
    def make_sound(self):
        return 'Мяу!'

obj1 = Dog()
obj2 = Cat()
obj3 = [Dog(), Cat()]
print(obj1.make_sound())
print(obj2.make_sound())
# for o in obj3:
#     print(o.make_sound())

'-----------------------------------------------------------'

class Employee(ABC):
    fixed_salary = 4000
    def __init__(self, bonus):
        self.bonus = bonus
    def calculate_salary(self):
        ...

class Developer(Employee):
    def calculate_salary(self):
        return super().fixed_salary + self.bonus

class Manager(Employee):
    def calculate_salary(self):
        return super().fixed_salary + self.bonus
    
sal_d = Developer(1000)
sal_m = Manager(3000)
print(sal_d.calculate_salary())
print(sal_m.calculate_salary())

'-----------------------------------------------------------'

class Database(ABC):
    def connect(self):
        ...
    def disconnect(self):
        ...

class MySQLDatabase(Database):
    def connect(self):
        return 'Подключение к MySQL'
    def disconnect(self):
        return 'Отключение от MySQL'
    
class PostgreSQLDatabase(Database):
    def connect(self):
        return 'Подключение к PostgreSQL'
    def disconnect(self):
        return 'Отключение от PostgreSQL'
    
my_sql = MySQLDatabase()
post_sql = PostgreSQLDatabase()
print(my_sql.connect())
print(my_sql.disconnect())
print(post_sql.connect())
print(post_sql.disconnect())
