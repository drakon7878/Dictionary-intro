class Car():
    color = ""
    model = ""
    brand = ""
    def __init__(self , color = "" , model = "" , brand = ""):
        self.color = color
        self.model = model
        self.brand = brand

    def upgrade(self):
        color = input("Type your new color here-->")
        self.color = color
        print("Details Updated, color is now "+self.color)

car1 = Car("red" , "350" , "Mahindra")
print(car1.brand)

car2 = Car()
print(car2.brand)

car1.upgrade()

