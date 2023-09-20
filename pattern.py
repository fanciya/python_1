              #increasing triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print()   


            #decreasing triangle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print('*',end='')
#     print()   


#pyramid of numbers upto 10
# n=5
# num=1
# for i in range(0,n):
#      for j in range(i+1):
#          print(num,end=' ') 
#          num=num+1
         
#      print()    




#alphabets
# value = 65
# for i in range(0, 5):
#     for j in range(0, i+1):
#         ch = chr(value)
#         print(ch, end=" ")
#         value = value + 1
#     print()


#hash hill
# n = 4
# for i in range(0, n):
#     for j in range(0,n-i-1):
#         print(end=' ')
#     for k in range(0, i +1):
#         print('#',end=' ')
#     print()

#even number pattern
# def print_number_pattern(rows):
#     num = 2
#     for i in range(1, rows + 1):
#         for j in range(i):
#             print(num, end=" ")
#             num += 2
#         print()
# rows = 4
# print_number_pattern(rows)

#character pattern
# rows = int(input("Enter number of rows: "))
# ascii_value = 65
# for i in range(rows):
#     for j in range(i+1):
#         alphabet = chr(ascii_value)
#         print(alphabet, end=" ")
#     ascii_value += 1
#     print("\n")

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end=" ")
        print()
    for i in range(rows - 1, 0, -1):
        for j in range(i):
            print('*', end=" ")
        print()

rows = 5
print_star_pattern(rows)
