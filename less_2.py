# # наследование 
# # полиморфизм
# # инкапсуляция



# class Human:
#     head=1
#     brain=True
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


#     def names (self):
#         self.names
#         print(self.num)

#     def __str__(self):
#         return f'name is {self.name} \n' \
#         f'age is {self.age}'

#     def __len__(self):
#         return len (self.name)

#     def num (self):
#         self.age = self.age * 2
#         print(self.age)

# class Student(Human):
#     def __init__(self, name, age,time):
#         super().__init__(name, age)
#         Human.__init__(name,age)
#         self.time = time
#     head = 2
#     def names(self):
#         super(Student,self).names()
#         print(len(self.name))


#     def main(self):
 
#         print("Эта функция класса студент")

# student = Student('Николай', 18)
# student.num()
# print(student)

# class Teacher(Student):...
# teach=Teacher('islam',18,8)













class Human:
    head = 1
    brain = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def names(self):
        print(self.name, self.age)

    def str(self):
        return f'name is {self.name} \n' \
               f'age is {self.age}'

    def len(self):
        return len(self.name)

    def num(self):
        self.age = self.age * 2
        print(self.age)
        print("Эта функция kласса people")
import time
class Student(Human):
    head = 2

    def __init__(self, name, age,):
        super().__init__(name, age)
        Human.__init__(self, age, name)
        self.time = time
 
    def names(self):
        super(Student, self).names()
        print(len(self.name))
    
    def main(self):
        print("Эта функция уласса студент")


student = Student("Николай", 20)
hum = Human("Beka", 19)
student.num()
print(student)

class Teacher(Student):
    def names(self):
        Human.names(self)

