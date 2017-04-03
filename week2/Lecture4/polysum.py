import math

PI = math.pi

def polysum(n, s):
    area = (0.25*n*s**2) / (math.tan(PI/n))
    perimeter = n * s
    result = area + perimeter**2
    
    return round(result, 4)


print(polysum(4, 10))
print(type(polysum(4, 10)))