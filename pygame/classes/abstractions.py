from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def desciption(self):
        print("This is a closed shape")
    
#myobj = Shape()

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side * self.side
        return area

mySq = Square(4)
print(mySq.area())
