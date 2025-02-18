#Python Math library
#1
import math

def degree_to_radian(degree):
    radian = degree * (math.pi / 180)
    return radian
degree = 15
radian = degree_to_radian(degree)

print(f"Input degree: {degree}")
print(f"Output radian: {radian:.6f}")

#2
def trapizoid_area(height, base1, base2):
    area = height * (base1 + base2)/ 2
    return area
height = 5
base1 = 5
base2 =6
area = trapizoid_area(height, base1, base2)

print(f"Height value: {height}")
print(f"First base value: {base1}")
print(f"Second base value: {base2}")
print(f"Area = {area}")

#3
def polygon_area(sides, length):
    area = (sides * length**2) / (4 * math.tan(math.pi / sides) )
    return area
sides = 4
length = 25
area = polygon_area(sides, length)

print(f"Polygon area = {area}")

#4
def parallelogram_area(length, height):
    return length * height
length = 5
height = 6
area = parallelogram_area(length, height)

print(f"Parallelogram area = {area}")
