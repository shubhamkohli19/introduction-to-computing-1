# Question-1

string = "Python is a case sensitive language"
print("We have given the string '{}'".format(string))
# Part (a) of Question-1
print("The Length of the string is {}".format(len(string)))  # len function is used to find the length of string
# Part (b) of Question-1
print("The Reversed order of the string is '{}'".format(string[-1::-1]))
# Part (c) of Question-1
sliced_string = string[10:26]  # Sliced and stored "a case sensitive" from the given string in the new string
print(sliced_string)
# Part (d) of Question-1
new_string = string.replace("a case sensitive", "object oriented")  # Replaced "a case sensitive" With "object oriented"
print(new_string)
# Part (e) of Question-1
print("The index of substring 'a' in the given string is {}".format(string.find('a')))
# Part (f) of Question-1
string_without_whitespaces = string.replace(" ", "")  # All the whitespaces has been removed from the given string
print("The given string without any whitespaces: '{}'".format(string_without_whitespaces))
print()

# Question-2

print("Welcome to this program")
print("Please Enter your details ")
name = input("Enter your name ")  # Stored my name
SID = int(input("Enter your Student ID number "))  # Stored my SID
Department = input("Enter your Department of Study ")  # Stored my department
CGPA = 9.9  # Stored the given CGPA in a variable
print("""Hey, {} Here!
My SID is {}
I am from {} department and my CGPA is {}""".format(name, SID, Department, CGPA))
print()

# QUESTION 3

print("This is a program to Calculate any two integers through Bitwise Operators.")
a = 56
b = 10
print("We have a = 56 and b = 10")
print("Now, using Bitwise Operators.")
# Part a of Question-3
print("a&b = ", a & b)
# Part b of Question-3
print("a|b = ", a | b)
# Part c of Question-3
print("a^b = ", a ^ b)
# Part d of Question-3
print("Left shift both a and b with 2 bits gives {} and {} respectively.".format(a << 2, b << 2))
# Part e of Question-3
print("Right shift 'a' with 2 bits and 'b' with 4 bits gives {} and {} respectively.".format(a >> 2, b >> 4))
print()

# Question-4

print("This is the program to find the greatest integer between any three numbers.")
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
num3 = int(input("Enter the third number "))
if (num1 >= num2) and (num1 >= num3):
    greatest_num = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest_num = num2
elif (num3 >= num1) and (num3 >= num2):
    greatest_num = num3
print("The greatest integer between {},{} and {} is {}".format(num1, num2, num3, greatest_num))
print()

# Question-5

print("This is the program to find out if your program has the word 'name' in it")
input_string = input("Enter a String ")
if "name" in input_string:
    print("Yes")  # Yes, the input entered by the user have the substring 'name' in it
else:
    print("No")  # No, the input entered by the user doesn't have the substring 'name' in it

# Question-6

print("This is the program to check if you can make a triangle with three input side values.")
first_side = int(input("ENTER FIRST SIDE OF THE TRIANGLE "))
second_side = int(input("ENTER SECOND SIDE OF THE TRIANGLE "))
third_side = int(input("ENTER THIRD SIDE OF THE TRIANGLE "))
if first_side >= (second_side + third_side):
    print("No")  # We cannot make a triangle with these three input sides
elif second_side >= (first_side + third_side):
    print("No")  # We cannot make a triangle with these three input sides
elif third_side >= (first_side + second_side):
    print("No")  # We cannot make a triangle with these three input sides
else:
    print("Yes")  # We can make a triangle with these three input sides
