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
print(hero.samatov("samat","spider","web",200,"sasat+lejat"))
print(hero.spiderman())
print(hero.health())
print(hero.get_name())
print(hero.len())
