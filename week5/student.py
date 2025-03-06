class Student:
    def __init__(self, name, grade_avg, student_id):
        self.__name = name
        self.__grade_avg = grade_avg
        self.__student_id = student_id
    
    def get_name(self):
        return self.__name
    
    def get_grade_avg(self):
        return self.__grade_avg
    
    def get_student_id(self):
        return self.__student_id
    
    def set_name(self, name):
        if name == '':
            print('Name cannot be empty')
        else:
            self.__name = name
    
    def set_grade_avg(self, grade_avg):
        if grade_avg < 0 or grade_avg > 100:
            print('Grade average must be between 0 and 100')
        else:
            self.__grade_avg = grade_avg
    
    def set_student_id(self, student_id):
        if student_id < 0:
            print('Student ID cannot be negative')
        else:
            self.__student_id = student_id
    
    def show(self):
        print('Name:', self.__name)
        print('Grade average:', self.__grade_avg)
        print('Student ID:', self.__student_id)