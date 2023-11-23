#给定一个字符串s，找到s中最长的回文子串。可以假设s的最大长度为1000。
#输入："babad" 输出："bab"
#输入："cbbd" 输出："bb"

def longestPalindrome(s):
    if not s:
        return ""

    n = len(s)
    start, max_length = 0, 1
    dp = [[False] * n for _ in range(n)]  #初始化动态数组

    for i in range(n):  #长度为1
        dp[i][i] = True

    for i in range(n - 1):  #长度为2
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    for length in range(3, n + 1): # 检查长度大于2的子串
        for i in range(n - length + 1):
            j = i + length - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                start = i
                max_length = length
    return s[start:start + max_length]

print(longestPalindrome("babad"))  
print(longestPalindrome("cbbd"))  
