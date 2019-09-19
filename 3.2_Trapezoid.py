'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
(base1+base 2)/2 *h
'''
print("welcome to your Trapezoid area calculator")
B1=int(input("What is the length of base 1?"))
B2=int(input("What is the length of base 2?"))
H=int(input("What is the height of your trapezoid?"))
B=(B1+B2)/2
area=B*H
print("The area of your trapezoid is",area)