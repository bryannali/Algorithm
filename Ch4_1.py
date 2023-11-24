#1 被读作“one 1”(一个一)，即11。
#11 被读作“two 1s”（两个一），即2。
#21 被读作“one 2，one 1”（一个二，一个一)，即1211。
#给定一个正整数n（1≤n≤30），输出外观数列的第n项。 注意：整数序列中的每一项将表示为一个字符串。

#输入：1 输出："1" 解释：这是一个基本样例。
#输入：4 输出："1211" 解释：当n=3时，序列是“21”，其中有“2”和“1”两组，“2”可以读作“12”，
#也就是出现频次为1，而值为2；类似于“1”可以读作“11”，所以答案是“12”和“11”组合在一起，也就是“1211”。

def countAndSay(n):
    if n == 1:
        return "1"

    prev_result = countAndSay(n - 1)
    result = ""
    
    count = 1
    for i in range(1, len(prev_result)):
        if prev_result[i] == prev_result[i - 1]: #统计相邻相同数字的个数
            count += 1
        else:
            result += str(count) + prev_result[i - 1] #生成新的字符串
            count = 1

    result += str(count) + prev_result[-1] #处理最后一组

    return result


print(countAndSay(1))  
print(countAndSay(4))  
