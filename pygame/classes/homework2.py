from abc import ABC , abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
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
    
    def perimeter(self):
        perimeter = self.side * 4
        return perimeter

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        area = self.radius * self.radius * 3.14
        return area

    def perimeter(self):
        perimeter = 2 * self.radius * 3.14
        return perimeter
    
class Triangle(Shape):
    """
    Where triangle is ABC \n
    side1  = AB of the triangle / BASE\n
    angle1 = angle CAB, meaning, it is point A where the angle is at\n
    side2 = BC of the triangle / PERPENDICULAR \n
    angle2 = angle ABC , angle is at B \n
    side3 = CA of the triangle / HYPOTENUSE \n
    angle3 =  angle ACB, angle is at C\n
    height = line from point C to AB in such a way that it is perpendicular to AB 
    """
    def __init__(self , side1 , side2, side3):
        self.AB = side1 #AB
        self.BC = side2 #BC
        self.CA = side3 #CA
        self.A = math.acos((self.CA**2 + self.AB**2 - self.BC**2)/(2 * self.CA * self.AB))
        self.B = math.acos((self.AB**2 + self.BC**2 - self.CA**2)/(2 * self.AB * self.BC)) 
        self.C = math.acos((self.CA**2 + self.BC**2 - self.AB**2)/(2 * self.CA * self.BC))
        self.height = self.CA * math.sin(self.A)
    def area(self):
        area = self.AB * self.height * 1/2
        return area
    def perimeter(self):
        perimeter = self.AB + self.BC + self.CA
        return perimeter

mySq = Square(5)
print(mySq.area())
print(mySq.perimeter())
myCircle = Circle(6)
print(myCircle.area())
print(myCircle.perimeter())
myTri = Triangle(17 , 13  , 12 )
print(myTri.area())
print(myTri.perimeter())
