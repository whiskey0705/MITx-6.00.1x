# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:28:13 2017

@author: Whiskey
"""
num = int(input('Please enter a number between 0 and 100 > \n'))

low = 0
high = 100
ans = (low + high) // 2
guess_num = 0

flag = True

msg = "Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly."

while flag:
    guess_num += 1
    print(f'Is your secret number {ans}?')
    confirm = input(f'{msg} \n>>>')
    if confirm == 'h':   
        high = ans
    elif confirm == 'l':
            low = ans
    elif confirm == 'c':
        flag = False
    else:
        print("I don't konw what you say!")
    ans = (low + high) // 2
print(f'Game over. Your secret number was: {ans}, it takes {guess_num} times')