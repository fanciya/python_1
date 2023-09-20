#1Write a program to check whether the entered number is postive or negative
# n=int(input("enter the number"))
# if n>=0:
#     print("the number is positive")
# else:
#     print("the number is negative")



#2.Write a program to  swap two variables.
# a=10
# b=5
# temp=a
# a=b
# b=temp
# print('The value of a after swapping: {}'.format(a))
# print('The value of b after swapping: {}'.format(b))



#3Write a program to  Determine If Year Is Leap Year
# year = int(input("Enter a year: "))
# if (year % 400 == 0) and (year % 100 == 0):
#     print("it  is a leap year")
# elif (year % 4 ==0) and (year % 100 != 0):
#    print("it is a leap year")
# else:
#     print("not a leap year")



#4Write a program check whether the given number is odd or even.
# a=int(input("enter the number"))
# if(a%2==0):
#     print("{} is even".format(a))
# else:
#     print("{} is odd".format(a))

   


#5.Write a program to print the fibonocci series.
# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1



#7. Write a program to print the prime numbers between given interval.
# lower=int(input("enter the lowest limit"))
# highest=int(input("enter the highest limit"))
# print("the prime numbers in the range are")
# for number in range(lower,highest+1):
#     if number>1:
#         for i in range(2,number):
#             if(number%i)==0:
#                 break
#         else:
#             print(number)




#8. Write a program for Printing Odd numbers between 1 and 50 and calculate the sum of that numbers.
# n=51
# sum = 0 
# for i in range(0,n+1): 
#    if(i%2!=0):
#       sum=sum + i 
#       print(sum)
 


#9. Write a program to find the factorial of the given number.
# n=int(input("enter the number"))
# fact=1
# if n<0:
#      print("factorial doesnt exist")
# elif n==0:
#      print("factorial of zero is 1")
# else:
#      for i in range(1,n+1):
#          fact=fact*i
# print(fact)




# 10.Write a program to Check if the given string  is Palindrome or not.
# string=input("enter the string")
# revstr=''
# for i in string:
#     revstr=i+revstr
#     print("reversed string:",revstr)
# if string==revstr:
#         print("string is palindrome")
# else:
#      print("string is not palindrome")





#11 Write a program to find sum of all integers greater than 100 and less than 200 that are divisible by 7.
# sum=0
# for i in range(100,201):
#     if i%7==0:
#         sum=sum+i  
# print(sum) 




#12.Write a program to Display Multiplication Table
# number = int(input ("Enter the number to print the multiplication table: "))      
# print ("The Multiplication Table of: ", number)    
# for count in range(1, 11):      
#    print (number, 'x', count, '=', number * count)    




#13. Write a program to calculate the area and perimeter of a rectangle..
# l=int(input("Length : "))
# b=int(input("Breadth : "))
# area=l*b
# perimeter=2*(l+b)
# print("Area of Rectangle : ",area)
# print("Perimeter of Rectangle : ",perimeter)  




#14. Write a program to find the sum of n' Natural Numbers.
# num = int(input("enter the number"))
# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is", sum)


#17. Write a program to remove all punctuations from given string.
# punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# my_str = input("enter a string:")
# no_punct=""
# for char in my_str:
#      if char not in punctuation:
#          no_punct=no_punct+char
# print(no_punct) 



#19. Write a program to count the no:of each vowel in a given string.
# text=input("enter the string")
# count=0
# for character in text:
#     if character in "aAeEiIoOuU":
#         count=count+1
# print("count of vowels:",count) 




# 16. Write a program to find the largest among 3 numbers.
# a=float(input("enter the first number:"))
# b=float(input("enter the second number:"))
# c=float(input("enter the third number:"))
# if a>b and a>c:
#     largest=a
# elif b>a and b>c:
#     largest=b
# else:
#    largest=c
# print("the largest number is:",largest)

    
#  15Python program to check if the number is an Armstrong number or not
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")


# 20. Program to perform Addition,Subtraction,Multiplication and division on Complex-No's.
# print("Addition of two complex numbers : ",(4+3j)+(3-7j))
# print("Subtraction of two complex numbers : ",(4+3j)-(3-7j))
# print("Multiplication of two complex numbers : ",(4+3j)*(3-7j))
# print("Division of two complex numbers : ",(4+3j)/(3-7j))


# 21. Find Value of the following expressions
# num_1 = 10
# num_2 = 11
 
# print(num_1 % num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)

# 22. Find the results of the following expressions (True or False)
# num_1=7
# num_2 = 6
 
# print(num_1 < num_2)
# print(num_1 > num_2)
# print(num_1 <= num_2)
# print(num_1 >= num_2)
# print(num_1==num_2)

   
# 23. Find the results of the following expressions (True or False)
# num_1=3
# num_2 = 4
 
# print((num_1 < num_2) and (num_1 != num_2))
# print((num_2 >= num_1) or (num_1 > num_2))
# print(not (num_1 == num_2))


# 24.  Output of the following while loop
# i=1
# while (i<6):
#     i = i +1
#     print(i) 
# 23456



# 25. Select the correct option
#  a INV-1212 INV-1215 INV-1218
# customer_num =5
# invoice_num =1212
# print("Invoice No(s):")
# while(customer_num >0):
#      print("INV -", invoice_num)
#      invoice_num = invoice_num +3
#      customer_num = customer_num -1


# 26. Write a python function to add ‘python’ at the end of a given string and return the new string. If the given string already ends with ‘python’ then add ‘java’. 
# If the length of the given string is less than 5, then add ‘php’.
def add_language(text):
    if text.endswith('python'):
        return text + 'java'
    elif len(text) < 5:
        return text + 'php'
    else:
        return text + 'python'
input_string =input("enter the string")
result = add_language(input_string)
print(result)

