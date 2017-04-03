def gcd_recur(a, b):
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)
    
print(gcd_recur(2, 12))
print(gcd_recur(6, 12))
print(gcd_recur(9, 12))
print(gcd_recur(17, 12))  