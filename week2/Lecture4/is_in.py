# astr是排序好的
def is_in(char, astr):
    if len(astr) == 0:
        return False
    if len(astr) == 1:
        return char == astr
    
    mid_index = len(astr)//2
    mid_char = astr[mid_index]
    
    
    if char > mid_char:
        return is_in(char, astr[mid_index+1:])
    elif char < mid_char:
        return is_in(char, astr[:mid_index])
    else:
        return True
    
print(is_in('o', 'abefow'))