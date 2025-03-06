from student import Student
from class_room import ClassRoom

class ClassManager:
    def __init__(self, class_name):
        # create a ClassRoom object with the given class name
        self.__class_room = ClassRoom(class_name)
    
    def print_menu(self):
        print('Class Manager')
        print('1. Add student')
        print('2. Delete student')
        print('3. Edit student')
        print('4. Show students')
        print('5. Exit')

    def add_student(self):
        print('Add Student')
        name = input('Enter student name: ')
        grade_avg = float(input('Enter student grade average: '))
        student_id = int(input('Enter student ID: '))
        # create a Student object
        st = Student(name, grade_avg, student_id)
        # add the student to the class room
        self.__class_room.add_student(st)
        print('Student added successfully')

    def delete_student(self):
        print('Delete Student')
        student_id = int(input('Enter student ID: '))
        # delete the student from the class room
        success = self.__class_room.delete_student(student_id)
        if not success: 
            print('Student not found')
        else:
            print('Student deleted successfully')
    
    def edit_student(self):
        print('Edit Student')
        student_id = int(input('Enter student ID: '))
        name = input('Enter new student name: ')
        grade_avg = float(input('Enter new student grade average: '))
        # edit the student in the class room
        success = self.__class_room.edit_student(student_id, name, grade_avg)
        if not success:
            print('Student not found')
        else:
            print('Student edited successfully')

    def show_students(self):
        # show all students in the class room
        self.__class_room.show_students()

    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1: self.add_student()
            elif choice == 2: self.delete_student()
            elif choice == 3: self.edit_student()
            elif choice == 4: self.show_students()
            elif choice == 5: running = False

if __name__ == '__main__':
    # create a ClassManager object and run it
    cm = ClassManager('Python Programming')
    cm.run()