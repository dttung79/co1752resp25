from student import Student

class ClassRoom:
    def __init__(self, name):
        self.__students = [] # list of Student objects initialized to empty list
        self.__name = name

    def get_name(self):
        return self.__name
    
    def add_student(self, st):
        self.__students.append(st)
    
    def find_student(self, student_id):
        for st in self.__students:
            if st.get_student_id() == student_id:
                return st
        return None
    
    def delete_student(self, student_id):
        # find the student with the given student_id
        st = self.find_student(student_id)
        # if the student is found, remove it from the list
        if st != None:
            self.__students.remove(st)
            return True
        return False
    
    def edit_student(self, student_id, name, grade_avg):
        # find the student with the given student_id
        st = self.find_student(student_id)
        # if the student is found, update its name and grade average
        if st != None:
            st.set_name(name)
            st.set_grade_avg(grade_avg)
            return True
        return False
    
    def show_students(self):
        # show all students in the class
        print('Class:', self.__name)
        print('-------- All Students ---------')
        for st in self.__students:
            st.show()
            print('-----------------')