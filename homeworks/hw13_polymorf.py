# class Document:
#     def print_info(self):
#         print('Doc')

# class PDFDocument(Document):
#     def print_info(self):
#         print('PDF')

# class WordDocument(Document):
#     def print_info(self):
#         print('Word')


# def print_document_info(doc):

#     for doc in objects:
#         doc.print_info()

# objects = [Document(), PDFDocument(), WordDocument()]
# print_document_info(objects)

'----------------------------------------------------------------'

# class Animal:
#     def make_sound(self):
#         ...

# class Dog(Animal):
#     def make_sound(self):
#         print('Гав')

# class Cat(Animal):
#     def make_sound(self):
#         print('Мяу')
    
# class Cow(Animal):
#     def make_sound(self):
#         print('Муу')

# def make_animals_talk(animal):
#     for animal in animals:
#         animal.make_sound()

# animals = [Dog(), Cat(), Cow()]
# make_animals_talk(animals)

'------------------------------------------------------------'

# class Toy:
#     def play_sound(self):
#         ...

# class Car:
#     def play_sound(self):
#         print('wroom')

# class Doll:
#     def play_sound(self):
#         print('hi')

# class Drum:
#     def play_sound(self):
#         print('dum')

# toys = [Car(), Doll(), Drum()]
# for toy in toys:
#     toy.play_sound()

'------------------------------------------------------------'

# class Shape:
#     def area(self):
#         ...

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return self.radius ** 2 * 3.14
        

# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def area(self):
#         return self.a * self.b

# class Triangle(Shape):
#     def __init__(self, a, h):
#         self.a = a
#         self.h = h

#     def area(self):
#         return self.a * self.h / 2
    
# cir = Circle(5)
# rec = Rectangle(3, 4)
# tri = Triangle(4, 5)

# figures = [cir, rec, tri]
# for figure in figures:
#     print(figure.area())

'------------------------------------------------------------'

class Card:
    def __init__(self, amount, drawed):
        self.amount = amount
        self.drawed = drawed
        
    def withdraw(self):
        return self.amount - self.drawed


class CreditCard(Card):
    def withdraw(self):
        return super().withdraw()
    
class DebitCard(Card):
    def withdraw(self):
        if self.amount - self.drawed >= 0:
            return super().withdraw()
        else:
            print('Exceed balance')

money = Card(100, 50)
credit = CreditCard(200, 50)
debit = DebitCard(100, 70) 

cash = [money, credit, debit]

for m in cash:
    print(m.withdraw())