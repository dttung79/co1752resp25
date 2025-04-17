class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == '':
            raise ValueError("Name cannot be empty")
        if len(value) > 20:
            raise ValueError("Name exceeds maximum 20 characters")
        self.__name = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 18:
            raise ValueError("Age cannot be less than 18")
        if value > 40:
            raise ValueError("Age exceeds maximum 40")
        self.__age = value
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")