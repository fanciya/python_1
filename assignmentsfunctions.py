
#1find odd or even using function
# def checkodd_even(number):
#     if number % 2==0:
#         print("the number is even")
#     else:
#         print("the number is odd")
# number=int(input("enter any number")) 
# checkodd_even(number)



#2dictionary using fnction squares
# def dict_sq(number):
#     number=dict()
#     for i in range(1,21):
#         number[i]=i**2
#     print(number)
# dict_sq(dict())

 #3string input list comprehension
# def remove_vowels(string):
#     string=input("enter the string")
#     vowels=["a","e","i","o","u","A","E","I","O","U"]
#     result=" ".join([char for char in string if char not in vowels])
#     return result
# print(remove_vowels("string"))


# 4. Write a program to display Powers of 2  using Anonymous functions?(lambda,map).
# terms=int(input("enter the number of terms"))
# result=list(map(lambda x: 2 ** x,range(terms)))
# print("the total terms are",terms)
# for i in range(terms):
#     print("2 raised to power", i, "is",result[i])      



# 7. Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.
# rank=[1,2,3]
# students=["ram","sam","sara"]
# dictionary=dict(zip(rank,students))
# print(dictionary)


# 9. Write a program to find the factorial of a number using recursion.
# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return(num*factorial(num-1))
# number=int(input("enter the number"))
# print("The factorial of", number, "is", factorial(number))


# 8.Write a program to print fibonocci series using recursion
# def rec_fibo(num):
#     if num<=1:
#         return num
#     else:
#         return(rec_fibo(num-1)+rec_fibo(num-2))
# nterms=int(input("enter the no: of terms"))
# if nterms<=0:
#     print("plz enter any positive numbers")
# else:
#     print("fibonacci sequence")
#     for i in range(nterms):
#         print(rec_fibo(i))


#16 Write a Python program to find the second smallest number in a list using function.
# li=[]
# n=int(input("enter the number of elements"))
# for i in range(1,n+1):
#     elem=int(input("enter the elements"))
#     li.append(elem)
# li.sort()
# print("the sorted list is:")
# print("The second smallest value of this list: ",li[1]) 

    

#12 Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.(implement generator)
# def evennumbers(n):
#  for i in range(0,n +1):
#   if i % 2 ==0:
#    yield i
# n=int(input("enter the limit"))
# result=evennumbers(n)
# print(next(result))
# print(next(result))
# print(next(result)) 
# print(next(result))
# print(next(result))

# 11 Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma sep
# arated form while n is input by console:
# def div5and7(n):
#  for i in range(0,n +1):
#    if i % 5 ==0 and i%7==0:
#       yield i
# print(list(div5and7(1000)))
 


# 6. bubblesort
# def bubbleSort(list):
#     for i in range(len(list)):
#         for j in range(0, len(list) - i - 1):
#             if list[j] > list[j + 1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp
# data = [8,2,4,1,5]
# bubbleSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)

# binary search algorithm

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
            return -1 
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 5
result = binary_search(sorted_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")

# 13 Write a program to implement Insertion-Sort algorithm in python.
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
# unsorted_list = [12, 11, 13, 5, 6]
# insertion_sort(unsorted_list)
# print("Sorted list:", unsorted_list)


# 14. Program to implement Linear-Search Algorithm.

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i 
#     return -1  
# my_list = [2, 4, 6, 8, 10, 12, 14, 16]
# target_element = 10
# result = linear_search(my_list, target_element)

# if result != -1:
#     print(f"Element {target_element} found at index {result}.")
# else:
#     print(f"Element {target_element} not found in the list.")  


# 15. Program to implement Selection-Sort Algorithm.
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
# unsorted_list = [64, 25, 12, 22, 11]
# selection_sort(unsorted_list)
# print("Sorted list:", unsorted_list)