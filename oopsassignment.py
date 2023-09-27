# 1. Define a class which has at least two methods one, 
# to get a string from console  input and other is to print the string in uppercase.


# class Iostring:
#     def __init__(self):
#         self.string="  "
#     def putdetails(self):
#         self.string=input("enter the string")
#     def getdetails(self):
#         self.string=print(self.string.upper())
# a=Iostring()
# a.putdetails()
# a.getdetails()            
                           
# 2. Define a class, which have a class parameter and have a same instance parameter.
# class Myclass:
#     class_param="iam a class parameter"
#     def __init__(self,instance_parameter):
#         self.instance_parameter=instance_parameter
# obj1=Myclass("instance1")
# obj2=Myclass("instance2")
# print("Class parameter:",Myclass.class_param)
# print("instance 1 Paramter",obj1.instance_parameter )
# print("instance 1 Paramter",obj1.instance_parameter )
       

# 4. Define a class named BankAccount. 
# This class should contain methods withdraw() and 
# deposit to calculate the balance amount remained in your account.

# class Bank_account:
#     def __init__(self,initial_balance):
#         self.balance=initial_balance
#     def deposit(self,amount):
#             if amount>0:
#                self.balance+=amount
#                print("the deposited amount is {}".format(self.balance))
#             else:
#                 print("insufficient amount")
#     def Withdraw(self,amount):
#         if 0<amount<=self.balance:
#             self.balance-=amount
#             print("withdrew amount is {}".format(self.balance))
#         else:
#             print("insufficient fund for withdrawal")
# Account=Bank_account(100000)  
# Account.deposit(5000)
# Account.Withdraw(200)

# super

# class Emp():
# 	def __init__(self, id, name, Add):
# 		self.id = id
# 		self.name = name
# 		self.Add = Add

# Class freelancer inherits EMP
# class Freelance(Emp):
# 	def __init__(self, id, name, Add, Emails):
# 		super().__init__(id, name, Add)
# 		self.Emails = Emails

# Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")
# print('The ID is:', Emp_1.id)

# print('The Name is:', Emp_1.name)
# print('The Address is:', Emp_1.Add)
# print('The Emails is:', Emp_1.Emails)



# 3. Define a class named Circle which can be constructed by radius. 
# The Circle class has a method which can compute the area.
# class Circle:
# 	def __init__(self,r):
# 		self.radius=r
# 	def area(self):
# 		return self.radius**2*3.14
# c=Circle(8)
# print(c.area())



# 5.Define a class named Shape and its subclass Square. 
# The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape 
# where Shape's area is 0 by default.

# class Shape:
#    def area(self): 
#     return 0
# class Square(Shape):
#      def __init__(self,l):
#          self.length=l
#      def area(self):
#        return self.length*2
# c=Square(2)
# print("area of the square",c.area())
# shape=Shape()
# print("the area of the shape:",shape.area())
			   

