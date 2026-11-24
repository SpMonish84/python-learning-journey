class Car:
    def __init__(self,name,year,color,speed_limit):
        self.Name = name
        self.year = year
        self.color = color
        self.speed_limit = speed_limit

    # methods
    def is_supercar(self):
        if self.speed_limit > 200:
            print("Its a Super Car")
        else:
            print("Its not a Super Car")

    def display(self):
        print(f"{self.Name} ({self.year}) - {self.color}")




Bmw = Car(name = " BMW GTR M3",year = 2017, color = "Blue and White", speed_limit = 340)
print(Bmw.Name)
print(Bmw.year)
print(Bmw.color)
print(Bmw.speed_limit)
Bmw.is_supercar()
Bmw.display()

