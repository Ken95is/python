
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_names(self):
        print('players in team:')
        for player in self.players:
            print(player.name)

player1 = Player('Alice') # создаю игроков
player2 = Player('Bob')
team = Team('My Team') # создаю команду
team.add_player(player1) # добавляю игроков
team.add_player(player2)
team.show_names() # показываю список игроков

'--------------------------------------------------'

class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self,employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f'Employees in {self.name}:')
        for emp in self.employees:
            print(emp.name)

    
employee = Employee('John')
A = Company('Company A')
B = Company('Company B')

A.add_employee(employee)
B.add_employee(employee)

A.show_employees()
B.show_employees()

'---------------------------------------------------'

class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        house = Room(room)
        self.rooms.append(house)

    def number_of_rooms(self):
        return len(self.rooms)
    
my_house = House()
my_house.add_room('1')
my_house.add_room('2')

print('number of rooms:', my_house.number_of_rooms())

'-----------------------------------------------------'

class Page:
    ...

class Book:
    def __init__(self, num_pages):
        self.pages = []
        
        for i in range(num_pages):
            self.pages.append(Page())
    
    def count_pages(self):
        return len(self.pages)
    
my_book = Book(3)
print('Pages in book:', my_book.count_pages())

'--------------------------------------------------'

class CPU:
    ...

class RAM:
    ...

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.cpu.name = 'Intel i7'
        self.ram.capacity = '16GB'

comp = Computer()

print('Computer has:')
print('CPU:', comp.cpu.name)
print('RAM:', comp.ram.capacity)

'-------------------------------------------------'

class Song:
    def __init__(self, title):
        self.title = title

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs_list = []

    def add_song(self, song):
        self.songs_list.append(song)

my_favorite_song = Song('Yesterday')

playlist = Playlist('Clasic Hits')
playlist.add_song(my_favorite_song)

del playlist

try:
    print(f"Song still exists: {my_favorite_song.title == 'Yesterday'}")
except:
    print('Song still exists: False')

'------------------------------------------------------------------------'

class Paragraph:
    count = 0 

    def __init__(self, text):
        self.text = text
        Paragraph.count += 1
        print(f'Paragraph created. Total paragraphs: {Paragraph.count}')

    def __del__(self):
        Paragraph.count -= 1 
        print(f'Paragraph deleted. Paragraphs left: {Paragraph.count}')

class Document:
    def __init__(self):
        self.paragraphs = []
        print('Document created')

    def add_paragraph(self, text):
        paragraph =  Paragraph(text)
        self.paragraphs.append(paragraph)

    def __del__(self):
        print(f'Deleting document with {len(self.paragraphs)} paragraphs')

