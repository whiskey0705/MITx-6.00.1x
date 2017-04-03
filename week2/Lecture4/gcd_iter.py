def gcd_iter(a, b):
    c = min(a, b)
    while a % c != 0 or b % c != 0:
        c -= 1
    return c

print(gcd_iter(2, 12))
print(gcd_iter(6, 12))
print(gcd_iter(9, 12))
print(gcd_iter(17, 12))