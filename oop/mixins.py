'======================================Миксины========================================'
# Миксины - это классы, которые будут использоваться для наследования. Но от миксинов не создаются обьекты. Классы помощники

class FlyMixin:
    def fly(self):
        print('я могу летать')

class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плавать')

class Human(WalkMixin, SwimMixin):
    name = 'человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыба'
    
class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'утка'


objects = [Human(), Fish(), Duck()]

for obj in objects:
    print(obj.name)
    attrs = ['fly', 'swim', 'walk', 'talk']
    for attr in attrs:
        if hasattr(obj, attr):
            method = getattr(obj, attr)
            method()
    print(' ')

obj = Human()
setattr(obj, 'telephone_number', '996222021103')
print(dir(obj))
print(obj.telephone_number)

# hasattr - функция, которая принимает обьект и название аттрибута. Возвращает True, если у обьекта есть такой аттрибут(метод)

# getattr - функция, которая принимает обьекты и названия аттрибута. Возвращает значение аттрибута

# setattr - функция которая принимает обьект, название аттриьута и значение для этого аттрибута. Добавляет в обьект новый аттрибут или перезаписывает одноименный аттрибут

