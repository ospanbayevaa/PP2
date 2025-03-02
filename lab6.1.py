#Python builtin functions 
#1
nums = [2, 3, 4, 5]
result = 1
for num in nums:
    result *= num 
print("multiply = ", result)

#2
def count_letters(num):
    upper_case = sum(1 for char in num if char.isupper())
    lower_case = sum(1 for char in num if char.islower())

    print("number of uppercase letters: ", upper_case)
    print("number of lowercase letters: ", lower_case)

text = "Hello KBTU!"
count_letters(text)

#3
def isPalindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1] 
text = "madam"

if isPalindrome(text):
    print("It's palindrome")
else:
    print("It is not a palindrome")

#4
import time
num = 25100
delay = 2123
time.sleep(delay/1000)
result = num ** 0.5
print(f"Square root of {num} after {delay} milliseconds is {result}")

#5
def all_elements_true(t):
    return all(t)
tuple1 = (True, True, 1, "Hello")
tuple2 = (False, True, 0, "Hello")
print(all_elements_true(tuple1))
print(all_elements_true(tuple2))

