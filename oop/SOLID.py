'======================================SOLID====================================='
# SOLID - это аббревиатура для набора принципов проектирования, созданных для разработки программного обеспечения при помощи обьектно-ориентированных языков.

# Принципы SOLID направлены на содействие разработки более простого, надежного и обновляемого кода

# S (SRP)
# 1. Single Responsibility Principle
# Принцип единственной обязанности
# Принцип единственной обязанности требует того, чтобы один класс выполнял одну работу (Т.е не надо создавать огромный класс который делает все)


# O (OCP)
# 2. Open-Closed Principle
# Принцип открытости/закрытости
# Программные сущности (классы, модули, функции) должны быть открыты для расширения, но закрыты для модификаций

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        if self.customer == 'simple':
            return '10%'
        elif self.customer == 'vip':
            return '20%'
        elif self.customer == 'premium':
            return '50%'
        elif self.customer == 'premium++':
            return '70%'

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

class SimpleDiscount(Discount):
    def get_discount(self):
        return f'{self} - 10%'
    
class VipDiscount(Discount):
    def get_discount(self):
        return f'{self} - 20%'
    
class PremiumDiscount(Discount):
    def get_discount(self):
        return f'{self} - 50%'
    
class PremiumPlusPlusDiscount(Discount):
    def get_discount(self):
        return f'{self} - 70%'
    

# L (LSP)
# Liskov Substitution Principle
# Принцип подстановки Лисков
# Главная идея в том, что для любого класса клиент должен иметь возможность использовать любой подкласс этого класса, не замечая разницы между ними. Это означает что клиент полностью изолирован и не подозревает об изменениях в иерархии классов

class Animal:
    def __init__(self, attrs):
        self.attributes = attrs

    def eat(self):
        print('Вкусно!')

class Cat(Animal):
    def eat(self, amount = 0.1):
        if amount > 0.3:
            print('Кошка сьела много')
        else:
            print('Кошке вкусно!')

class Dog(Animal):
    def eat(self):
        print('Собаке вкусно!')

pluto = Dog({'name':'Pluto', 'age': 3})
goofy = Dog({'name': 'Goofy', 'age': 2})
button = Cat(('Mr.Buttons', 4))

# animals = (pluto, goofy, button)

# for animal in animals:
#     if animal.attributes['age'] > 2:
#         print(animal.attributes['name'])

# I (ISP)
# Interface Segregetion Principle
# Принцип разделения интерфейсов
# Создавайте тонкие интерфейсы, которые ориентированы на клиента. Клиент не должен зависеть от интерфейсов(или же методов которые не используются). Этот принцип устраняет недостатки реализации больших интерфейсов


class Creature:
    def __init__(self, name):
        self.name = name

    def swim(self):
        ...
        
    def walk(self):
        ...

    def talk(self):
        ...

class Human(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} - умеет плавать')

    def walk(self):
        print(f'{self.name} - умеет ходить')

    def talk(self):
        print(f'{self.name} - умеет говорить')

class Fish(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} - умеет плавать')

class Cat(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} - умеет плавать')

    def walk(self):
        print(f'{self.name} - умеет ходить')

human = Human('John Smith')
human.talk()
human.walk()
human.swim()

fish = Fish('Nemo')
fish.swim()
fish.walk()
fish.talk()

cat = Cat('ASD')
cat.walk()
cat.swim()
cat.talk()

'-------------------------------------------------------'

class SwimInterface:
    def swim(self):
        ...

class WalkInteface:
    def walk(self):
        ...

class TalkInterface:
    def talk(self):
        ...

class Human(SwimInterface, TalkInterface, WalkInteface):
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f'{self.name} - умеет плавать')

    def walk(self):
        print(f'{self.name} - умеет ходить')

    def talk(self):
        print(f'{self.name} - умеет говорить')


# D (DIP)
# Dependency Inversion Principle
# Принцип Инверсии Зависимостей
# Зависимость должна быть от абстракций, а не от конкретики.
# Модули верхних уровней не должны зависить от модулей нижних уровней. Классы и верхних и нижних уровней не должны зависить от одних и тех же абстракций. Абстракции не должны зависеть от деталей. Детали должны зависить от абстракций
