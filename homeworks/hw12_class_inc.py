class BankAccount:
    
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, deposit):
        self.__balance = self.__balance + deposit

    def withdraw(self, sum):
        if sum < self.__balance:
            self.__balance -= sum
    
    def get_balance(self):
        return self.__balance


obj1 = BankAccount()
obj1.deposit(1000)
obj1.withdraw(300)
print(obj1.get_balance())


# '----------------------------------------------------------------------------------------------'

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def get_password(self):
        return '*' * len(self.__password)
    
    def set_password(self, new_password):
        if self.__password.isalnum and len(new_password) > 6:
            self.__password = new_password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

obj = User('tim', '1234tim')
# print(obj.password)
# print(obj.name)
# obj.password = '6543'
# print(obj.password)
# obj.name = 'bob'
# print(obj.name)
print(obj.get_password())
# print(obj.set_password())

# '------------------------------------------------------------------------------------------'

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 30000:
            self.__salary = salary
        else:
            print('Error')


emp = Employee('Bob', 30000)
print(emp.name)
emp.salary = 20000
print(emp.salary)



# '------------------------------------------------------------------------------------------------'

class Circle:
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            print('Error')

    def area(self):
        return self.radius ** 2 * 3.14
    
class Cylinder(Circle):
    def __init__(self, height):
        if height > 0:
            self.height = height

shape = Circle(5)
print(shape.area())