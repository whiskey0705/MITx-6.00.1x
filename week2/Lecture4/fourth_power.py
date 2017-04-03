def square(x):
    return x**2

def fourth_power(x):
    """
    调用2次square()， 即把square()结果作为参数传入square()里
    """
    return square(square(x))

power4 = fourth_power(2)
print(power4)