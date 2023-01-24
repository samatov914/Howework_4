# q = 'qwerty'
# c = 1
# print(type(q))
# print(type(c))


def name (a):...
class Human:
    head=1
    brain=True
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def names (self):
        print(self.name)

    def __str__(self):
        return f'name is {self.name} \n' \
        f'age is {self.age}'

    def __len__(self):
        return len (self.name)

    def num (self):
        self.age = self.age * 2
        print(self.age)

c=Human



hum=Human('Samat',16)
hum.names()

print(len(hum))

hum2=Human ('ali',15)
print(hum2)
print(len(hum2))

print(hum)