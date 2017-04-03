# 将用户输入的数字转换为int，然后赋值给cube
cube = int(input('enter a num > '))
# 初始化guess的值为0
guess = 0



# while循环满足的条件是guess的3次方小于cube的绝对值
    # 进去的是guess， 出来的是guess+1
    # 假设cube对于27， guess变化
    # 进入        出来
    # 0          1
    # 1          2
    # 2          3
    # 3  由于不满于条件了， 跳出while循环， 最终guess为3
while guess**3 < abs(cube): 
    guess += 1
    
# 如果guess的三次方不等于cube的绝对值，说明这不是一个完美的cube
if guess**3 != abs(cube):
    print(f'{cube} does not have a cube root')
# else说明两者相等， 如果cube是负数，那么guess也要转化为负的
else:
    if cube < 0:
        guess = -guess    
    print(f'the root for cube{cube} is {guess}')