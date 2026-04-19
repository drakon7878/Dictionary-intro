class CarType():
    def __init__(self , type = "Sedan" , color = "White"):
        self.type = type
        self.color = color

class Car(CarType):
    def __init__(self, type = "Sedan", color = "White", model = "Basic"):
        super().__init__(type  , color )
        self.model = model
    
    def wheelDrive(self , driveWheel = "Front"):
        self.driveWheel = driveWheel

mycar = Car("XUV" , "Red" , "4500U")
mycar.wheelDrive("Back")
mycar2 = Car(color="Blue" , model= "5300H")
mycar2.wheelDrive()
print(mycar.color + "\n"+ mycar.driveWheel + '\n' +mycar.type +"\n")
print(mycar2.color + "\n"+ mycar2.driveWheel + '\n' +mycar2.type )
