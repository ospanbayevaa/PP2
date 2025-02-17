 #Python iterators and generators
#1
def square_generator(N):
    for i in range(N+1):
     yield i ** 2
print(list(square_generator(5)))

#2
n = int(input("Enter a number: "))
def even_number(n):
    yield from range(0, n+1, 2)
print(", ".join(map(str, even_number(n))))

#3
def divisible_num(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter a number: "))
print("Numbers divisible by 3 and 4:")
for num in divisible_num(n):
    print(num)

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2
a, b = map(int, input(). split())
for square in squares(a, b):
    print(square)

#5
def from_down(n):
    for i in range(n, -1, -1):
        yield i
for num in from_down(15):
    print(num, end=" ")






