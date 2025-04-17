from student import Student

def test_student_01():
    st = Student("John", 20)
    assert st.name == "John"
    assert st.age == 20

def test_student_02():
    try:
        st = Student("", 20)
        raise Exception("Test failed: No exception raised for empty name")
    except ValueError as e:
        assert str(e) == "Name cannot be empty"

def test_student_03():
    try:
        st = Student("John", 17)
        raise Exception("Test failed: No exception raised for age < 18")
    except ValueError as e:
        assert str(e) == "Age cannot be less than 18"

def test_student_04():
    try:
        st = Student("A very long name that exceeds the maximum length", 20)
        raise Exception("Test failed: No exception raised for name exceeding 20 characters")
    except ValueError as e:
        assert str(e) == "Name exceeds maximum 20 characters"

def test_student_05():
    try:
        st = Student("John", 41)
        raise Exception("Test failed: No exception raised for age > 40")
    except ValueError as e:
        assert str(e) == "Age exceeds maximum 40"

def test_student_06():
    try:
        st = Student(20, 20)
        raise Exception("Test failed: No exception raised for invalid name type")
    except TypeError as e:
        assert str(e) == "Name must be a string"

def test_student_07():
    try:
        st = Student("John", "20")
        raise Exception("Test failed: No exception raised for invalid age type")
    except TypeError as e:
        assert str(e) == "Age must be an integer"

def test_student_08():
    try:
        st = Student("John", 20.0)
        raise Exception("Test failed: No exception raised for invalid age type")
    except TypeError as e:
        assert str(e) == "Age must be an integer"

def test_student_09(capsys):
    st = Student("John", 20)
    st.show_info()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Name: John, Age: 20"
