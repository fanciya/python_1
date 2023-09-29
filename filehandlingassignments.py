# 3. Write a program to  solve Quadratic Equation ?

import math
# a= float(input("enter the coefficient of x^2(a):"))
# b= float(input("enter the coefficient of x(b):"))
# c= float(input("enter the constant term(c):"))
# discriminant=b*2 - 4*a*c
# if discriminant>0:
#     root1 = (-b + math.sqrt(discriminant)) / (2*a)
#     root2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print(f"the roots real and distinct: {root1} and {root2}")
# elif discriminant==0:
#     root1 = -b / (2*a)
#     print(f"The root is real and repeated: {root1}")
# else:
#     realPart = -b / (2*a)
#     imaginaryPart = math.sqrt(-discriminant) / (2*a)
#     print(f"The roots are complex: {realPart} + {imaginaryPart}i and {realPart} - {imaginaryPart}i")


# 4. Write a program to perform read and write operation on a CSV File ?
# import csv
# with open("C:/Users/thasm/Desktop/book2.csv",'r') as file:
#      reader=csv.reader(file)
#      for row in reader:
#          print (row)

# import csv
# with open('C:/Users/thasm/Desktop/Book2.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])
#     writer.writerow([1, "M.T", "NAALUKETTU"])
#     writer.writerow([2, "ROBIN SHARMA", "THE MAN WHO SOLD HIS FERRARI"])
#     writer.writerow([3, "RHONDA BYRNE", "THE SECRET"])


# 1. Write a program to create a new file and write data to it

# file_name = "new_file.txt"
# try:
#     with open(file_name, "w") as file:
       
#         file.write("This is a new file.\n")
#         file.write("You can write any data you want to it.\n")
#         file.write("This is another line in the file.\n")
#         file.write("And one more line for good measure.")
#     print(f"Data has been written to {file_name} successfully.")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")



# 2. Write a program to read data from a file ? (using read() and readline())?
# f = open("C:/Users/thasm/Desktop/demo.txt", "r")
# print(f.read())
# f = open("C:/Users/thasm/Desktop/demo.txt", "r")
# print(f.readline())
# f.close()

# 6. Write a program to append data to an existing file 

# file_name = "newfile.txt"
# try:
#     with open(file_name, "a") as file:
#         # Append data to the file
#         file.write("This is new data appended to the existing file.\n")
#         file.write("You can keep adding more data to it.\n")
#     print(f"Data has been appended to {file_name} successfully.")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# 5. Write a program to write JSON data to a file ?
import json
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


file_name = "data.json"


try:
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)
    print(f"JSON data has been written to {file_name} successfully.")
except Exception as e:
    print(f"An error occurred: {e}")




