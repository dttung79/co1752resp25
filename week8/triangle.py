from shape import Shape

class Triangle(Shape):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self._shape_type = "Triangle"
        self._side_a = a
        self._side_b = b
        self._side_c = c
    
    def area(self):
        p = (self._side_a + self._side_b + self._side_c) / 2
        s = (p * (p - self._side_a) * (p - self._side_b) * (p - self._side_c)) ** 0.5
        return s
    
    def __str__(self):
        return super().__str__() + f'Sides: ({self._side_a:.2f}, {self._side_b:.2f}, {self._side_c:.2f})'
    
class EquiTriangle(Triangle):
    def __init__(self, name, side):
        super().__init__(name, side, side, side)
        self._shape_type = "Equilateral Triangle"
    
    @property
    def side(self):
        return self._side_a # or self._side_b or self._side_c
    
    @side.setter
    def side(self, side):
        self._side_a = side
        self._side_b = side
        self._side_c = side
