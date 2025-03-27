from shape import Shape
import math

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)          # Call the constructor of the Shape class
        self._shape_type = "Circle"
        self.__radius = radius        # __radius is a private attribute

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    # Overriding the area method to calculate the area of a circle
    def area(self):
        return math.pi * self.__radius ** 2
    
    # Overriding the __str__ method to return the additional info of the circle (radius)
    def __str__(self):
        return f'{super().__str__()}. Radius: {self.__radius:.2f}'
    
if __name__ == "__main__":
    c = Circle("C", 5)
    print(c) # this will call method __str__ and print the info of the circle
