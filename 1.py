import random

def guess_number():
    while True:
        name = input("Hello! What is your name? ")
        number = random.randint(1, 20)
        print(f"Well, {name}, I am thinking of a number between 1 and 20.")
        guesses = 0
        while True:
            try:
                guess = int(input("Take a guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            guesses += 1
            if guess < number:
                print("Your guess is too low.")
            elif guess > number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
                break
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break


def is_high_rated(movie):
    return movie["imdb"] > 5.5

def high_rated_movies(movies):
    return [movie for movie in movies if is_high_rated(movie)]

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def average_imdb(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

def category_average_imdb(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)


class StringHandler:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Enter a string: ")
    
    def printString(self):
        print(self.s.upper())

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 0.5)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

filter_prime_lambda = lambda numbers: list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))
