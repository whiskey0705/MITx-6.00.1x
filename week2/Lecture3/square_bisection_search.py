# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:28:13 2017

@author: Whiskey
"""

x = 25
epsilon = 0.01
low = 0
high = x
ans = (low + high) / 2
guess_num = 0

while abs(ans**2 - x) >= epsilon:
    
    print(f'low: {low}, high: {high}, ans: {ans}')
    if ans**2 < x:
        low = ans
    elif ans** 2 > x:
        high = ans
    else: 
        # 因为精确度是0.01， 所以几乎不可能有相等的情况，所以可以
        # 只考虑大于和小于的情况，只用if-else就可以了
        print('find answer')
    ans = (low + high) / 2
    guess_num += 1

print(f'{ans} is close to square root of {x}, it takes {guess_num} times.')