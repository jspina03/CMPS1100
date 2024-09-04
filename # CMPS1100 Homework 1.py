# CMPS1100 Homework 1

# write a function that calculates the area of a circle, gievn its radius
import math
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)
radius = 5
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area: .2f}")

# write a function that calculates the area of a square, given its length
def calculate_square_area(length):
    return length ** 2
length = 4 
area = calculate_square_area(length)
print(f"The area of the square with length {length} is {area}")

# using the previous 2 functions to answer the question: "what has more area, a circle with a radius 2 or a square with a side length 3?"
import math
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)
def calculate_square_area(length):
    return length **2
# given values
radius = 2
side_length = 3 
# calculate areas
circle_area = calculate_circle_area(radius)
square_area = calculate_square_area(side_length)
# compare areas
if circle_area > square_area:
    result = "The circle has a larger area."
elif circle_area < square_area: 
    result = "The square has a larger area."
else:
    result = "The circle and the square have the same area."
# output the result 
print(f"circle area: {circle_area:.2f}")
print(f"square area: {square_area:.2f}")
print(result)

