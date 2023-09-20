# 1. Write a program to find the transpose of a matrix.
# X = [[12,7],
#     [4 ,5],
#      [3 ,8]]
# result = [[0,0,0],
#           [0,0,0]]
# for i in range(len(X)):
#    for j in range(len(X[0])):
#     result[j][i] = X[i][j]
# for r in result:
#        print(r)

# 2. Write a program that accepts sequence of lines as input and prints the 
# lines after making all characters in the sentence capitalized:

# lines = []
# while True:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break;
# for l in lines:
#     print(l)
	

# 3. Write a program to implement all built-in methods of list.


# 4. Write a program to read dictionary values through keyboard and merge two dictionaries.
# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 4: 'd'}
# print(dict_1 | dict_2)

# 5.Write a program to demonstrate all built-in methods of dictionary.


# 6. Write a program to find the sum of all the elements in a list.
# list = [12, 8, 9, 2, 5]
# print(list)
# print("sum of list: ",sum(list))

# 7. With a given integral number n, write a program to generate a dictionary that contains(i,i*i) such that i is an 
# integral number between 1 and n. And then the program should print the dictionary::
# number = int(input("Type a number: "))
# numberDict = {}
# for i in range(1, number+1):
#     numberDict[i] = i*i
# print(numberDict)

# 8. Write a program that accepts a sentence and calculate the number of letters & digits
# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1 
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)

# 9. Write a program to implement filter(), map() and reduce() .
from functools import reduce

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter: Filter even numbers
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered numbers (even):", filtered_numbers)

# Map: Square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Reduce: Calculate the sum of all numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)

# from functools import reduce
# nums=[1,2,3,4]
# ans= reduce(lambda x,y:x+y,nums)
# print(ans)
# ages=[5,20,35,25,40,65,50]
# def myfunc(x):
#     if x < 18:
#         return False
#     else:
#         return True
    
# adults=filter(myfunc,ages)
# for x in adults:
#   print(x)
# numbers=[1,2,3,4,5,6]
# def odd(number):
#     return number%2!=0
# odd_numbers=map(odd,numbers)
# print(list(odd_numbers))
    
# 10. Write a program to implement List Comprehension .
# number_list = [ x for x in range(20) if x % 2 == 0]
# print(number_list)


# 11. Write a program to implement Dictionary Comprehension ..
# square_dict = {num: num*num for num in range(1, 11)}
# print(square_dict)

# 12. Write a program to find the largest and smallest element from a list.
# lst = []
# num = int(input('How many numbers: '))
# for n in range(num):
#     numbers = int(input('Enter number '))
#     lst.append(numbers)
# print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

# 13. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
# num = [7,8, 120, 25, 44, 20, 27]
# num = [x for x in num if x%2!=0]
# print(num)

# 14. Write a Python program to generate and print a list of first 
# and last 5 elements where the values are square of numbers between 1 and 30
# l = list()
# for i in range(11,25):
# 	l.append(i**2)
# print(l[:5])
# print(l[-5:])

# 15. Write a Python program to insert a given string at the beginning of all items in a list. 
# num = [1,2,3,4]
# print(['emp{0}'.format(i) for i in  num])

# 16.  Write a Python program to iterate over two lists simultaneously.
# num = [1, 2, 3]
# color = ['red', 'white', 'black']
# for (a,b) in zip(num, color):
#      print(a, b)

# 17.  Write a Python program to add a key to a dictionary.
# d = {0:10, 1:20}
# print(d)
# d.update({2:30})
# print(d)



# 18Write a Python script to concatenate following dictionaries to create a new one.

    #    Sample Dictionary :
    #           dic1={1:10, 2:20}
    #           dic2={3:30, 4:40}
    #           dic3={5:50,6:60} 
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)



# 19. Write a Python program to iterate over dictionaries using for loops.
# dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
# for key, value in dt.items():
#     print(key, value)


# 20. Write a Python program to sum all the items in a dictionary.
# my_dict = {'data1':100,'data2':-54,'data3':247}
# print(sum(my_dict.values()))




# 21.  Create a dictionary to hold information about pets. Each key is an animal's name, 
# and each value is the kind of animal.Eg : {'Dog':'Willie'}
# Put at least 3 key-value pairs in your dictionary.
# Use a for loop to print out a series of statements such as "Willie is a dog."


# pets = {
#     'Dog': 'Willie',
#     'Cat': 'Whiskers',
#     'Fish': 'Nemo'
# }
# for animal, name in pets.items():
#     print(f"{name} is a {animal}.")

# 22. Write a python function to create and return a new dictionary from the given dictionary (subject: mark).
# Create a new dictionary with subject having marks more than 50.
# marks = {English: 40,'Maths': 60, 'Hindi: 30,'Chemistry': 46,'Physics': 70}

# def filter_marks_above_50(marks):
#     filtered_marks = {}
#     for subject, mark in marks.items():
#         if mark > 50:
#             filtered_marks[subject] = mark
#     return filtered_marks
# marks = {'English': 40, 'Maths': 60, 'Hindi': 30, 'Chemistry': 46, 'Physics': 70}
# filtered_dict = filter_marks_above_50(marks)
# print(filtered_dict)


# 23Write a python function which accepts a sentence and finds the 
# number of letters and digits in the sentence.
# # It should return a dictionary in 
# which the key should be letter count and value should be digit count. 
# Ignore the spaces or any other special character in the sentence.


# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)

#  24Write a Python function which generates and returns a dictionary where the keys are numbers 
# between 1 and n (both inclusive) and the values are square of keys.

# def generate_dict(number):
# 	new_dict={}
# 	for i in range(1,number+1):
# 		new_dict[i]=i*i
# 		return new_dict

# number=20
# print(generate_dict(number))

