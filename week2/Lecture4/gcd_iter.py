def gcd_iter(a, b):
    c = min(a, b)
    # 当a除以c余数为0，并且b除以c余数为0时，while条件为False or False,即跳出循环
    while a % c != 0 or b % c != 0:
        c -= 1
    return c

print(gcd_iter(2, 12))
print(gcd_iter(6, 12))
print(gcd_iter(9, 12))
print(gcd_iter(17, 12))