#Sign your name:Emma E. Moritz___


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
print("Nice to meet you!",firstname,lastname)

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
B=int(input("What is the base of your triangle?"))
H=int(input("What is the height of your triangle?"))
Area=(B*H)/2
print("The area of your triangle is", Area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
ra=int(input("What is the radius of your circle?"))
cir=2*3.14*ra
print("Your circumference is", cir)

# 4. Ask a user for an integer and then print the square root.

A=int(input("What is your number?"))
B=A**.5
print("The square root of your number is",B)
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

M=int(input("What is the Mass?"))
A=int(input("What is the Acceleration?"))
F=M*A
print("Your force is",F)
print("Get it?")