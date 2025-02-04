#Python Classes

import math
#1
class StringChange:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Enter a string: ")
    
    def printString(self):
        print(self.text.upper())

str1 = StringChange()
str1.getString()
str1.printString()

#2
class Shape:
    def area(self):
        return 0
class square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length**2
sq = square(5)
print(sq.area())    

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return  self.length * self.width
rect = Rectangle(4,6)
print(rect.area())

#4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point({self.x}, {self.y})")
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other_point):
            return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
p1 = Point(1, 2)
p2 = Point(4, 5)

p1.show()
p2.show()
print(p1.dist(p2))

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} added. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return False
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
            return True


acc = Account("Adina", 100)
acc.deposit(50)     
acc.withdraw(30)   
acc.withdraw(200)   

#6
nums = input().split()
nums = [int(num) for num in nums]

def is_prime(num):
    if num<2:
        return False
    else:
        for i in range (2, num//2+1):
            if num%i == 0:
                return False
        return True
    
prime_nums = list(filter(lambda x: is_prime(x), nums))
print(prime_nums)