class SuperHero:
    people = 'people'
    def samatov(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def spiderman(self):
        return f"name: {self.name}"
    def health(self):
        return f"name: {self.name}, health: {self.health_points * 2}"
    def get_name(self):
        return f"nick: {self.nickname}, super: {self.superpower}, health: {self.health_points}"
    def len(self):
        return f"length: {len(self.catchphrase)}"
hero = SuperHero()
print(hero.samatov("samat","spider","web",200,"lejat+sasat"))
print(hero.spiderman())
print(hero.health())
print(hero.get_name())
print(hero.len())




# HW 2



class JusticeLeague(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    
    def hitpoints(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        print("HP:", self.health_points)
    def phrase(self):
        print(f"Hero flyes:{self.fly}")

c = JusticeLeague("Bryse","Batman","Money",100,"Do you know who I am, scum?",150)
c.hitpoints()
c.phrase()

class Avengers(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    
    def hitpoints(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        print("HP:", self.health_points)
    def phrase(self):
        print(f"Hero flyes:{self.fly}")
    
b = Avengers("Tony Stark","Iron Man", "Brain,money",200,"I dont paint",500)
b.hitpoints()
b.phrase()

class Villain(Avengers):
    people = "Monster"
    def gen_x(self):
        pass
    
    def crit_DMG(self):
        crit = self.damage ** self.damage
        print("Crit Damage:", crit)
        
d = Villain
print(d.people)