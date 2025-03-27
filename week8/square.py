from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        # Call the constructor of the Rectangle class, passing the side as width and height
        super().__init__(name, side, side)
        self._shape_type = "Square"
    
    @property
    def side(self):
        return self._width   # or self.height, since they are the same
    
    @side.setter
    def side(self, side):
        self._width = side
        self._height = side

if __name__ == '__main__':
    s = Square("ABCD", 5)
    print(s)
    s.side = 10
    print(s)