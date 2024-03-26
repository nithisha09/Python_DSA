class StarCookie:
    brand = "ParleG"
    def __init__(self,color,count=100,cream=0):
        self.color = color
        self.count = count
        self.cream = cream
    def add_cream(self,cream):
        self.cream += cream

cookie_1 = StarCookie("Brown")
cookie_2 = StarCookie("White",10)
print(cookie_1.__dict__)
print(cookie_2.__dict__)
cookie_2.brand = "Sunfeast"
print(cookie_2.brand)
print(StarCookie.__dict__)
print(StarCookie.__module__)


cookie_3 = StarCookie("Black",25,2)
cookie_3.add_cream(3)
print(cookie_3.cream)

