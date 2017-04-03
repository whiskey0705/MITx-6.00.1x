# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:00:53 2017

@author: Whiskey
"""

x = 25
epsilon = 0.01
step = 0.001
guess = 0
guess_num = 0

while abs(guess**2 - x) >= epsilon:
    guess += step
    guess_num += 1
    
if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print(f'{guess} is close to square root of {x}, it takes {guess_num} times.')