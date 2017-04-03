# string = 'bob'
# s = input('enter a str > \n')
# s = s.lower()
# # str.count()只统计不叠加的，
# # s = 'azcbobobegghakl'，显示1而不是题目要求的2
# count = strings.count(string)

# print(f'Number of vowels: {count}')


s = 'azcbobobegghakl' #长度为15
word = 'bob'
count = 0
"""
字符串	3个字母顺序组合     组合数量     
ABC 	ABC					1	(3-2)
ABCD	ABC BCD				2	(4-2)
ABCDE	ABC BCD CDE			3	(5-2)
. 		.                   .
.       .                   .
.       .                   .
也就是说，字符串长度为N，就有(N-2)种连续的3个字母的组合

"""

# 由于字符串s的长度为15， 根据上面的推导，s有13种组合情况
# range()从0开始, 但不包括end。所以for循环里i的值从0开始一直到12
# 然后通过切片，每次加1对s取三个字符串，满足条件的话count就加1
for i in range(len(s)-2):
	# print(s[i:i+3])
	if s[i:i+3] == word:
		count += 1

print(f'Number of vowels: {count}')
