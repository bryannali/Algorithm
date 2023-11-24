#给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。

#输入："bbbab" 输出：4 一个可能的最长回文子序列为"bbbb"。

#输入："cbbd" 输出：2 一个可能的最长回文子序列为"bb"。

def longestPalindromeSubseq(s):
    if not s:
        return 0

    n = len(s)
    dp = [[0] * n for _ in range(n)] #初始化数组
    
    for i in range(n): #长度为1的子序列是回文
        dp[i][i] = 1

    
    for length in range(2, n + 1): # 从长度为2开始往下算
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]: #如何相等，
                dp[i][j] = dp[i + 1][j - 1] + 2 #长度+2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) #取两个方向的最大值
    return dp[0][n - 1]


print(longestPalindromeSubseq("bbbab"))  
print(longestPalindromeSubseq("cbbd"))  
