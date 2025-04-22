import json

def validate_password(password):
    if len(password) < 8:
        raise Exception('Пароль слишком короткий')
    if not password.isalnum():
        raise Exception('Пароль должен состоять из букв и цифр')

class RegisterMixin:
    def register(self, id, name, password):
        count = 1
        id = count
        self.name = name
        self.password = password
        validate_password(password)

        user = {'id': id, 'name': self.name, 'password': self.password}
        count += 1

        with open('user.json') as file:
            users = json.load(file)
            for user in users:
                if user['name'] == name:
                    raise Exception('Такой юзер уже сущуствует!')
                else:
                    with open('user.json', 'a') as file:
                        print('Succesfully registered')
                        json.dump(user, file, indent=4)


class LoginMixin:
    def login(self, name, password):
        with open('user.json') as file:
            users = json.load(file)
            for user in users:
                if user['name'] != name:
                    print('Нет такого юзера в БД!')
                elif user['name'] == name:
                    if user['password'] != password:
                        print('Неверный пароль')
                    else:
                        print('Вы успешно залогинились!')


class ChangePasswordMixin:
    def change_password(self, name, old_password, new_password):
        validate_password(new_password)
        with open('user.json') as file:
            users = json.load(file)
            for user in users:
                if user['password'] != old_password:
                    raise Exception('Старый пароль указан неверно!')
                else:
                    with open('user.json', 'a') as file:
                        for user in users:
                            user['password'] == new_password
                            return 'Password changed successfully!'
                        json.dump(user, file, indent=4)


class ChangeUsernameMixin:
    def change_name(self, old_name, new_name):
        with open('user.json') as file:
            users = json.load(file)
            for user in users:
                if old_name != user:
                    raise Exception('Нет такого зарегистрированного юзера в БД!')
                else:
                    with open('user.json', 'a') as file:
                        for user in users:
                            while old_name == user:
                                print('Пользователь с таким именем уже существует!')
                                new_name = input('Введите новое имя')
                        user['name'] = new_name
                        json.dump(user, file, indent=4)
                        return 'Username changed successfully!'
        

class User(RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin):
    ...
    

class CheckOwnerMixin:
    def check(self, owner):
        with open('user.json') as file:
            users = json.load(file)
            for user in users:
                if user['name'] != owner:
                    raise Exception('Нет такого пользователя!')
                else:
                    ...


class Post(CheckOwnerMixin):
    def __init__(self, title, description, price, quantity, owner):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = owner



