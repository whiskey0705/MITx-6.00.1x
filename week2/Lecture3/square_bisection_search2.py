# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:28:13 2017

@author: Whiskey
"""
# 0 < x < 1
x = 0.04
epsilon = 0.01
low = 0
high = 1
ans = (low + high) / 2
guess_num = 0

while abs(ans**2 - x) >= epsilon:
    
    print(f'low: {low}, high: {high}, ans: {ans}')
    if ans**2 < x:
        low = ans
    else: 
        high = ans
    ans = (low + high) / 2
    guess_num += 1

print(f'{ans} is close to square root of {x}, it takes {guess_num} times.')