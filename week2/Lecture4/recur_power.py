def recur_power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recur_power(base, exp-1)
    
print(recur_power(3, 3))