# Question-1
print("Welcome. This is a program to find the average of three numbers. ")
num1 = input("Enter first number")
num2 = input("Enter second number")
num3 = input("Enter third number")
average: float = (int(num1) + int(num2) + int(num3)) / 3
print("The average of three numbers is :")
print(average)
print()

# Question-2
print("Welcome. This is a program to find your Income Tax.")
standard_deduction = 10000
depend_deduction = 3000
gross = input("Enter your gross Income(in $)")
Number_of_dependents = input("Enter your number of dependents")
taxable_income = int(gross) - int(standard_deduction) - (int(depend_deduction) + int(Number_of_dependents))
tax = (float(taxable_income) * 0.2)
print("Your Income Tax is :")
print("$" + str(tax))
print()

# Question-3
print("Please fill in the required details:")
SID = input("Enter your SID")
Name = input("Enter your name")
Gender = input("Enter your Gender: 'M','F','U'(for Unknown)")
Course_name = input("Enter your course name")
CGPA = float(input("Enter your CGPA"))
print()

# Question-4
marks = []
for i in range(5):  # For loop to take input 5 times
    marks.append(input("Enter marks of student " + str(i + 1)))
marks.sort()
print(marks)
print()

# Question-5
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Solution of part (a) of this question is:")
color.remove(color[3])
print(color)
print("\nSolution of part (b) of this question is:")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5] = ['Purple']
print("Part b of question :", color)
