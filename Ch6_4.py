#实现 int sqrt(int x)函数。
# 计算并返回x的平方根，其中x是非负整数。
# 由于返回类型是整数，结果只保留整数部分，小数部分将被舍去。

#输入：8输出：2

def mySqrt(x):
    if x == 0 or x == 1:
        return x

    left, right = 1, x

    while left <= right:
        mid = left + (right - left) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

result = mySqrt(8)
print(result)  
