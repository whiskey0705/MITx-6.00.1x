animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(a_dict):
    """
    返回所有value的个数
    """
    num = 0
    for k in a_dict.keys():
        num += len(a_dict[k])
    return num

print(how_many(animals))


