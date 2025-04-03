from shape import Shape
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle, EquiTriangle

def main():
    c = Circle("C", 5)
    r = Rectangle("ABCD", 5, 10)
    s = Square("MNPQ", 5)
    t = Triangle("XYZ", 3, 4, 5)
    et = EquiTriangle("PQR", 5)

    shapes = [c, r, s, t, et]

    for shape in shapes:
        print(shape)
        print('---------------------------------')

if __name__ == "__main__":
    main()