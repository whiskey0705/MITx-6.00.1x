def remove_dups(list1, list2):
	"""
	remove elements from list1 which in list2
	"""
	copy_list1 = list1[:]

	for ele in copy_list1:
		if ele in list2:
			list1.remove(ele)

lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 5, 6]

remove_dups(lst1, lst2)
print(lst1)