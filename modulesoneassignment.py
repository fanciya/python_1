# 1)Create a person with a method speak that prints "Hello Iam person".Then create  
# 2 classes Teacher & Student  that inherits from Person.Teacher should have a method  teach that prints 
# "Iam teaching",while student should have  a method learn that prints 
# "Iam learning".Finally create  an instance of Teacher and student and call their methods to demonstrate their functionalitites?

class Person:
    def speak(self):
        print("Hello, I am a person.")

class Teacher(Person):
    def teach(self):
        print("I am teaching.")

class Student(Person):
    def learn(self):
        print("I am learning.")


teacher_instance = Teacher()
student_instance = Student()


teacher_instance.speak()  
teacher_instance.teach()  

student_instance.speak()  
student_instance.learn()  
