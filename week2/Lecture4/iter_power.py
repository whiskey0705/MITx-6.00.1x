def iter_power(base, exp):
    result = 1
    for i in range(1, exp+1):
        result *= base
    return result
        
print(iter_power(2, 3))