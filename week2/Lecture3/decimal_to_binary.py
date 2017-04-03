init_num = int(input('enter a number >'))

num = init_num
if num < 0:
	is_neg = True
	num = abs(num)
else:
	is_neg = False

result = ''

if num == 0:
	result = '0'
while num > 0:
	result = str(num % 2) + result
	num = num // 2
if is_neg:
	result = '-' + result

print(f'{init_num} <10 to 2> is {result}')
