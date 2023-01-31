class A:
    def __init__(self,name):
        self.name = name
class B:
    def __init__(self,age):
        self.age = age
class C:
    def a():
        pass
class D:
    def b():
        pass
class Sam(A,B,C,D):
    def __init__(self, name,age):
        A.__init__(self,name)
        B.__init__(self,age)
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"
sam = Sam("samat",18)
print(sam)