def is_palindrome(s):
    
    def tochars(s):
        s = s.lower()
        ans = ''
        alphabet = 'abcdefghijkmnopqrstuvwxyz'
        for c in s:
            if c in alphabet:
                ans += c
        return ans
    
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1]) # 利用and的短路特性
    return is_pal(tochars(s))