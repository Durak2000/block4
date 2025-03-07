import math


def circle_fits_in_triangle(circle_area, triangle_area):
    r = math.sqrt(circle_area / math.pi)
    h = math.sqrt(3) / 2 * (2 * math.sqrt(triangle_area / (math.sqrt(3) / 4))) ** (1/2)
    r_inscribed = h / 3
    return r <= r_inscribed


def triangle_fits_in_circle(circle_area, triangle_area):
    R = math.sqrt(circle_area / math.pi)
    a = math.sqrt(triangle_area / (math.sqrt(3) / 4))
    R_circumscribed = a / math.sqrt(3)
    return R >= R_circumscribed


circle_area = int(input('Введите радиус: '))
triangle_area = int(input('Введите сторону треугольника: '))

print("Круг уместится в треугольнике:", circle_fits_in_triangle(circle_area, triangle_area))
print("Треугольник уместится в круге:", triangle_fits_in_circle(circle_area, triangle_area))
