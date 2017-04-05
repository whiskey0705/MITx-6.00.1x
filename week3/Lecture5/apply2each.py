def apply2each(a_list, fn):
	"""
	把list里的每个元素传入fn，新生成的元素代理原来的元素
	"""
	for i in range(len(a_list)):
		a_list[i] = fn(a_list[i])


def add1_multiplication2(n):
	return (n + 1) * 2

lst = [1, 2, 3]

apply2each(lst, add1_multiplication2)

print(lst)


###############################

def all2one(a_list, n):
	"""
	list是一组函数， 对n应用每一个函数并把结果添加到一个数组里，返回数组
	"""
	result = []
	for i in a_list:
		result.append(i(n))
	return result

mlist = [abs, add1_multiplication2, int, str]

print(all2one(mlist, -25.5))
