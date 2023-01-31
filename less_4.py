# # # # МНожественное наследование

# # # class Учитель:
# # #     def учить(self = 1):
# # #         print('я умею учить')


# # # class Строитель:
# # #     def строить(self = 1):
# # #         print('я умею строить')

# # # class Ученик(Учитель,Строитель):...


# # # c = Ученик
# # # c.учить()
# # # c.строить

# # class A:
# #     def __init__ (self,s):
# #         self.s = s
# #     def a(self = 1):
# #         print('A')

# # class B:
# #     def a(self = 1):
# #         print('B')

# # class C(B,A):
# #     def a(self = 1):
# #         print('C')

# # a = C('s')
# # a.a()
# # print(C.__mro__)



# class A:
#     def __init__(self,name):
#         self.name = name
#     def run(Self):
#         print('run A')

# class B(A):
#     def __init__ (self,age):
#         self.age = age

#     def run(self):
#         print('run B')

# class C(B):...


class O: ... 
class A(O): ... 
class B(O): ... 
class C(O): ... 
class D(O): ... 
class E(O): ... 
 
class K1(A, B, C): ... 
class K2(B, D): ... 
class K3(C, D, E): ... 
 
class Z(K1, K2, K3):...

