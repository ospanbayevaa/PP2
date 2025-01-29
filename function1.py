#Python Function 1
#1
def grams_to_ounces(grams):
    return grams * 28.3495231
print(grams_to_ounces(20))

#2
def fahrenheit_to_celsious(f):
    return (5 / 9) * (f - 32)
print(fahrenheit_to_celsious(120))

#3
def solve(numheads, numlegs):
    for chicken in range(numheads + 1):
        rabbits = numheads - chicken
        if(chicken * 2 and rabbits * 4) == numlegs:
            return chicken, rabbits
        return None
print(solve(35, 94))

#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
        return True
def filter_prime(numbers):
    return[num for num in numbers if is_prime(num)]
print(filter_prime([10, 3, 5, 23, 21]))

#5 
from itertools import permutations

def string_permutations():
    user_input = input("Enter a string: ")
    perms = [''.join(p) for p in permutations(user_input)]
    print("\n".join(perms))

#string_permutations()

#6
def reverse_sentence():
    user_input = input("Enter a sentence: ")
    reversed_sentence = " ".join(user_input.split()[::-1])
    return reversed_sentence

#print(reverse_sentence())

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#9
def sphere_volume(radius):
    return (4/3 * 3.14 * (radius**3))
print(sphere_volume(3))

#10
def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
print(unique_list([1, 2, 3, 1, 2, 4]))  

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("Hello"))
print(is_palindrome("Level"))

#12
def histogram(lst):
    for num in lst:
        print('*' * num)
histogram([4, 9, 7])

#13
import random
def guess_number():
    name = input("Hello! what's your name?\n")
    number = random.randint(1, 20)
    print(f"Well, {name}, I'm thinking of a number between 1 and 20.")

    attempts = 0
    while True:
        guess = int(input("Take a guess.\n"))
        attempts += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
guess_number()





