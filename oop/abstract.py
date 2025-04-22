'================================Абстракция===================================='
# Абстракция - это принцип ооп, в котором мы создаем класс пустышку, где задаем названия аттрибутов и методов, для того, чтобы в дочерних классах не забыть их переопределить


from abc import ABC, abstractmethod, abstractproperty

class AbstractAnimal(ABC):
    # @abstractproperty
    @property
    @abstractmethod
    def legs(self):
        ...

    @abstractmethod
    def voice(self):
        ...

# obj = AbstractAnimal() - НЕЛЬЗЯ

class Dog(AbstractAnimal):
    ...

# obj1 = Dog() # Ошибка, потому что нужно переопределять в классе Dog метод voice и аттрибут legs

class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print('Гав-гав')

# obj2 = Dog()
# print(obj2.legs)
# obj2.voice()

class Employee:
    name = 'katana'
    salary = '1000000'

class Manager(Employee):
    department = 'KATANA'
    def show_info(self):
        print(super().name, super().salary, self.department)

# obj = Manager()
# obj.show_info()

'-------------------------------------------------------------'

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, deposit):
#         self.deposit = self.__balance + deposit


class Student:
    
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_value):
        self.__name = new_value


    # def grade(self, grade):
    #     if self.__grade >= 0 and self.__grade <= 100:
    #         self.__grade = grade 
    #     else:
    #         print('Error')
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, new_value):
        if 100 >= new_value >= 0:
            self.__grade = new_value
        else:
            print('Error')

stud = Student('katana', 13)
# stud.grade = 100
# print(stud.grade)
# stud.grade = 200
# print(stud.grade)
# stud.grade = 50
# print(stud.grade)

'------------------------------------------------------------------'

class Dog:
    def speak(self):
        print('гав-гав')

class Cat:
    def speak(self):
        print('мяу-мяу')

animals = [Dog(), Cat()]

# def make_sound(animals):

# animals.make_sound()
for pet in animals:
        pet.speak()


# class Shape:
#     def area(self):
#         ...

# class Rectangle:
#     ...

# class Circle:
#     ...