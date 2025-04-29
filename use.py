from library.figures import Circle, Triangle

circle = Circle(5)
print(f"Площадь круга: {circle.area():.2f}")

triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.area():.2f}")
print(f"Прямоугольный? {triangle.is_right()}")
