class Shape:
    def __init__(self, name):
        self._shape_type = "General Shape"
        self._name = name
    
    # Default implementation for area, returns 0 because cannot calculate area of a general shape
    def area(self):
        return 0   
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    # Overriding the __str__ method to return the info of the shape
    def __str__(self):
        return f'{self._shape_type}: {self._name}. Area: {self.area():.2f}'

if __name__ == "__main__":
    s = Shape("A")
    print(s) # this will call method __str__ and print the info of the shape
    