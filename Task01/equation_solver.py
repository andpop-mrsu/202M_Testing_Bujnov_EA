import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return None  # Бесконечно решений
            else:
                return []    # Решений нет
        else:
            return [-c / b]  # Линейное уравнение
    else:
        D = b**2 - 4*a*c
        if D < 0:
            return []
        elif D == 0:
            x = -b / (2*a)
            return [x]
        else:
            sqrt_D = math.sqrt(D)
            x1 = (-b - sqrt_D) / (2*a)
            x2 = (-b + sqrt_D) / (2*a)
            return sorted([x1, x2])