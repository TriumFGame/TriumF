def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits

def filter_prime(numbers):
    return [num for num in numbers if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    return any(nums[i] == nums[i + 1] == 3 for i in range(len(nums) - 1))

def spy_game(nums):
    pattern = [0, 0, 7]
    for num in nums:
        if num == pattern[0]:
            pattern.pop(0)
        if not pattern:
            return True
    return False

def sphere_volume(radius):
    return (4 / 3) * 3.14159 * (radius ** 3)

def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

def is_palindrome(s):
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

import random

def guess_number():
    name = input("Hello! What is your name? ")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess: "))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


def is_high_rated(movie):
    return movie["imdb"] > 5.5

def high_rated_movies(movies):
    return [movie for movie in movies if is_high_rated(movie)]

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

def category_average_imdb(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies) if category_movies else 0


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
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

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

filter_prime_lambda = lambda numbers: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))
