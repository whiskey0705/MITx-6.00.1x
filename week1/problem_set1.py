# 将5个元音字母放入元组VOWELS里
VOWELS = ('a', 'e', 'i', 'o', 'u')
# 初始化count的值为0
count = 0
# 让用户输入一个字符串
string = input('enter a str > \n')
# 将字符串统一格式化为小写字母
string = string.lower()
# 循环遍历字符串， 如果i在VOWELS里，说明找到了元音字母，count加1
for i in string:
	if i in VOWELS:
		count += 1

print(f'Number of vowels: {count}')