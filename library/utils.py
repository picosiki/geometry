def is_right_triangle(a: float, b: float, c: float, epsilon: float = 1e-6) -> bool:
    sides = sorted([a, b, c])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < epsilon
