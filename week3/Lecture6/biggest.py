animals = { 'a': ['aardvark'], 
            'b': ['baboon'], 
            'c': ['coati'], 
            'd':['donkey', 'dog', 'dingo']}



def biggest(a_dict):
    """
    返回字典最长value对应的key
    """
    # 初始化结果为None，即如果字典为空则返回None
    result = None
    # value值长度的参考标准，初始化为0
    num = 0
    for k in a_dict.keys():
        # 如果value的长度比num大
        if len(a_dict[k]) > num:
            # 就把当前的key赋给result
            result = k
            # 然后把参考标准调整为当前的长度
            num = len(a_dict[k])
    return result

print(biggest(animals))