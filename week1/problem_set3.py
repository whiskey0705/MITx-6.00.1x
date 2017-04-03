# s = 'aa'
# s = 'abcbcd'
s = 'azcbobobegghakl'

# 初始化切片的起始和终止下标
# 新建一个空的列表，用于后面筛选最长字符串
start = 0
end = 0
ls = []

"""
注意：切片[:]和range()都是不包括end的，因为后续比较涉及到i+1，
为了防止超出range()的范围，这里要len()-1

i      s[i] and s[i+1]   s[start: end]   start  end
0	   s[0]     s[1]     
		a   <=   z	     s[0:2]          0      i+2=2

1	   s[1]     s[2]	 
        z    >   c      不符合要求      i+1=2

2	   s[2]     s[3]     
		c    >   b	    不符合要求      i+1=3   

3	   s[3]     s[4]	 
        b    <=    o     s[3:5]         继承    i+2=5

"""    


for i in range(len(s)-1):
	# 比较i和i+1位置的2个字母，如果满足s[i] <= s[i+1]，
	if s[i] <= s[i+1]:
		# 将end赋值为i+2，正好截取比较的这2个字符
		end = i + 2
		word = s[start: end]
		# 将截取的字符添加到数组， 继续循环
		ls.append(word)
	# 如果不满足前面的条件，说明不是按照alpha排列，所以start要重置
	# 为end位置的字符
	else:
		start = i + 1

print(ls)

# 设置一个标杆，len()为0
flag = ''
# 循环数组，只要该元素的len比flag大，就赋值给flag
for j in ls:
	if len(flag) < len(j):
		flag = j

print(f'Longest substring in alphabetical order is: {flag}')
