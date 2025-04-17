from my_functions import add, subtract, divide, sum

def test_add_01():
    # define inputs
    a = 1
    b = 2
    # define expected output
    expected = 3
    # assert expected output equals actual output by calling the function
    assert add(a, b) == expected

def test_add_02():
    a = 1
    b = 0
    expected = 1
    assert add(a, b) == expected

def test_subtract_01():
    a = 5
    b = 3
    expected = 2
    assert subtract(a, b) == expected

def test_subtract_02():
    a = 0
    b = 0
    expected = 0
    assert subtract(a, b) == expected

def test_divide_01():
    a = 4
    b = 2
    expected = 2
    assert divide(a, b) == expected

def test_divide_02():
    a = 10
    b = 2
    expected = 5
    assert divide(a, b) == expected

def test_divide_03():
    a = 2
    b = 10
    expected = 0.2
    assert divide(a, b) == expected

def test_divide_04():
    a = 0
    b = 10
    expected = 0
    assert divide(a, b) == expected

def test_divide_05():
    a = 10 ** 6
    b = 1
    expected = 10 ** 6
    assert divide(a, b) == expected

def test_divide_06():
    a = 1
    b = 10 ** 6
    expected = 0.000001
    assert divide(a, b) == expected

def test_divide_07():
    a = 10
    b = 0
    expected = "Cannot divide by zero"
    try:
        divide(a, b)
        assert False, "Expected exception but got none" # if no exception, test fails
    except Exception as e:
        assert str(e) == expected   # if exception raised but not the expected message, test fails


def test_sum_01():
    n = 10
    expected = 55
    assert sum(n) == expected

def test_sum_02():
    n = 1
    expected = 1
    assert sum(n) == expected

def test_sum_03():
    n = 2
    expected = 3
    assert sum(n) == expected

def test_sum_04():
    n = 0
    expected = "Error: n < 1"
    try:
        sum(n)
        assert False, "Expected exception but got none" # if no exception, test fails
    except Exception as e:
        assert str(e) == expected   # if exception raised but not the expected message, test fails

def test_sum_05():
    n = -10
    expected = "Error: n < 1"
    try:
        sum(n)
        assert False, "Expected exception but got none" # if no exception, test fails
    except Exception as e:
        assert str(e) == expected   # if exception raised but not the expected message, test fails