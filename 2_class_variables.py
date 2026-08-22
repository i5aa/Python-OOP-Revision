#Task 1

class Car:
    wheels = 4
    cars_in_garage = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        Car.cars_in_garage+=1

    def describe(self):
        print(f'{self.brand} {self.model} has {self.wheels} wheels')

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3= Car("Porsche", "911 GT3 RS")
car1.describe()
car2.describe()
car3.describe()
print(Car.wheels)
print(Car.cars_in_garage)


#Task 2

class Game:
    high_score = 0

    def __init__(self,player_name,score):
        self.player_name = player_name
        self.score = score

    def check_high_score(self):
        if self.score > Game.high_score:
            Game.high_score = self.score

g1 = Game("Alice", 500)
g1.check_high_score()

g2 = Game("Bob", 800)
g2.check_high_score()

g3 = Game("Carl", 300)
g3.check_high_score()

print(Game.high_score)

#Task 3

class Employee:
    raise_percent = 1.05

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def give_raise(self):
        self.salary *= self.raise_percent
        print(self.salary)

e1 = Employee("Sam", 50000)
e1.give_raise()
e2 = Employee("Alex", 60000)
e2.give_raise()
e3 = Employee("Jo", 55000)
e3.give_raise()

#Task 4

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    total_books_borrowed = 0

    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)

    def borrow_book(self, title):
        for book in self.catalog:
            if book.title == title:
                self.catalog.remove(book)
                Library.total_books_borrowed += 1
                return
        print(f"'{title}' not found in catalog.")


lib = Library()
lib.add_book(Book("1984", "Orwell"))
lib.add_book(Book("Dune", "Herbert"))

lib.borrow_book("1984")
print(Library.total_books_borrowed)  
print(len(lib.catalog))               


