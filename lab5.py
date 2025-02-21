#ReGex
#1
import re

pattern = r'ab*'

test_string = input("Enter a string: ")

if re.fullmatch(pattern, test_string):
    print("Match found!")
else:
    print("No match.")

#2
import re
pattern = r"ab{2,3}$"
test_strings = ["abb", "abbb", "a", "ab", "abbbb", "b", "aabb"]

for test in test_strings:
    if re.fullmatch(pattern, test):
        print(f"'{test}' matches the pattern")
    else:
        print(f"'{test}' does not match the pattern")

#3
import re

pattern = r"[a-z]+_[a-z]+"

text = input("Enter a string: ")

if re.fullmatch(pattern, text):
    print("Match found!")
else:
    print("No match.")

#4
import re
pattern = r"[A-Z][a-z]+"
txt = input("Enter a string: ")

if re.fullmatch(pattern, txt):
    print("Match found!")
else:
    print("No match")

#5
import re

pattern = r"a.*b$"
txt = ["ab", "axxxxb", "a123b", "abc"]

for test in txt:
    if re.fullmatch(pattern, test):
        print(f"{test} matches")
    else:
        print(f"{test} not match")

#6
import re

pattern = r"[ ,.]"
text = input("Enter a string: ")

result = re.sub(pattern, ":", text)
print("Result: ", result)

#7
import re
def snakeToCamel(snakeStr):
    camelStr = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snakeStr)
    return camelStr

text = input("Enter a camel-case string: ")
print("Camel-case string: ", snakeToCamel(text))

#8
import re
def split_to_upper(text):
    result = re.split(r'(?=[A-Z])', text)
    return result
text = input("Enter a string: ")
print("Split list: ", split_to_upper(text))

#9
import re
def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
input_text = "HelloKBTU"
text = insert_spaces(input_text)
print(text)

#10
import re
def camelToSnake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

input_text = "HelloWorld"
output_text = camelToSnake(input_text)
print(output_text) 
