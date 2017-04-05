def fib(n):
    """
    普通递归斐波那契数列
    """
    global fib_count
    fib_count += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_count = 0    
print(f'fib: {fib(30)}', f'count: {fib_count}')

print('#'*20)

def fib_efficiency(n, a_dict={0:1, 1:1}):
    global fib_eff_count
    fib_eff_count += 1
    if n in a_dict:
        return a_dict[n]
    else:
        result = fib_efficiency(n-1, a_dict) + fib_efficiency(n-2, a_dict)
        a_dict[n] = result
        return result
 
fib_eff_count = 0
print(f'fib_eff: {fib_efficiency(30)}', f'count: {fib_eff_count}')