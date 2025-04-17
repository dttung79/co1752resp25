def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b
    return c

def divide(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        raise Exception("Cannot divide by zero")

def sum(n):
    if n < 1:
        raise Exception("Error: n < 1")
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

if __name__ == "__main__":
    print(10/0)