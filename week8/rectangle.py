from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, w, h):
        super().__init__(name)          # Call the constructor of the Shape class
        self._shape_type = "Rectangle"
        self._width = w        # __width is a protected attribute
        self._height = h        # __height is a protected attribute

    # TODO: implement properties for width and height
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, w):
        self._width = w

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, h):
        self._height = h
    # TODO: implement the area method to calculate the area of a rectangle
    def area(self):
        return self._width * self._height

    # TODO: implement the __str__ method to return the additional info of the rectangle (width and height)
    def __str__(self):
        return f'{super().__str__()}. Width: {self._width:.2f}, Height: {self._height:.2f}'
    
if __name__ == "__main__":
    r = Rectangle("ABCD", 5, 10)
    print(r)