# 枚举法求平方根
x1 = 25
ans1 = 0
APPROX = 0.1
step = 0.01
guess_num1 = 0

while abs(ans1**2 - x1) >= APPROX:
    ans1 += step
    guess_num1 += 1
    
if (ans1**2 - x1) >= APPROX:
    print('failed')
else:
    print(f'{ans1} is close to square root of {x1} ')
print(f'it takes {guess_num1} times')
print('#'*30)


# 2分法求平方根
x2 = 25
low = 0
high = x2
ans2 = (low + high) / 2
guess_num2 = 0
       
while abs(ans2**2 - x2) >= APPROX:
    if ans2**2 < x2:
        low = ans2
    else:
        high = ans2
    ans2 = (low + high) / 2
    guess_num2 += 1

print(f'{ans2} is close to square root of {x2} ')
print(f'it takes {guess_num2} times')
print('#'*30)


# 牛顿法

"""

"""



x3 = 25
ans3 = x3/2
guess_num3 = 0

while abs(ans3**2 - x3) >= APPROX:
    ans3 = ans3 - (ans3**2 - x3) / (2 * ans3)
    guess_num3 += 1
    
if (ans3**2 - x1) >= APPROX:
    print('failed')
else:
    print(f'{ans3} is close to square root of {x3} ')
print(f'it takes {guess_num3} times')
print('#'*30)
                  
              







