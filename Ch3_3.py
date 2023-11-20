#判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#输入：121 输出：True
#输入：-121 输出：False

def isPalindrome(x):
    
    str_x = str(x) # 将整数转换为字符串
    
    return str_x == str_x[::-1]

print(isPalindrome(121))    # 输出 True
print(isPalindrome(-121))   # 输出 False
