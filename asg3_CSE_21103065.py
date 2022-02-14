# Question-1
print("This is the program to count the number of occurrences of each word in the string")
string = input("Enter a string-")
list1 = []
list2 = string.split()
length = len(list2)
d1 = dict()
d2 = dict()
print("The outcome of number of occurences of each word in the given string is:")
if len(list2) == 1:  # It is for a single word string
    for i in string:
        list1.append(i)
    for j in list1:
        if j in d1:  # Get value 1 and when a key repeats it increases
            d1[j] = d1[j] + 1  # Value added by 1
        else:
            d1[j] = 1
    print(d1)


else:
    for i in list2:  # This is for more than a word
        if i in d2:
            d2[i] = d2[i] + 1
        else:
            d2[i] = 1
    print(d2)
print()

# Question-1
print("This is the program to count the number of occurrences of each word in the string")
string = input("Enter a string: ")
list1 = []
list2 = string.split()
length = len(list2)
d1 = dict()
d2 = dict()
print("The outcome of number of occurrences of each word in the given string is:")
if len(list2) == 1:  # It is for a single word string
    for i in string:
        list1.append(i)
    for j in list1:
        if j in d1:  # Get value 1 and when a key repeats it increases
            d1[j] = d1[j] + 1  # Value added by 1
        else:
            d1[j] = 1
    print(d1)
