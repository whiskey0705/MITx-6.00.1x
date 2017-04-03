cube = int(input('enter a num > '))
num_guess = 0
# guess的值从0开始，每次循环加1，一直到guess=cube
for guess in range(abs(cube) + 1):
    # 与while循环不同，不存在进去guess出来guess+1的说法
    # 当guess的三次方大于或等于cube时，说明要么当前的guess就是root，
    # 要么就不是完美cube，然后跳出循环
    if guess**3 >= abs(cube):   
        break
    num_guess += 1
if guess**3 != abs(cube):
    print(f'{cube} does not have a cube root')
else:
    if cube < 0:
        guess = -guess
    print((f'the root for cube{cube} is {guess}'))
print(f'num_guess:{num_guess}')

