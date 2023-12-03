#珂珂喜欢吃香蕉。这里有n堆香蕉，第i堆中有piles[i]根香蕉。警卫已经离开了，将在h小时后回来。
#珂珂可以决定她吃香蕉的速度k（单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉k根。
#如果这堆香蕉少于k根，她将吃掉这堆里的所有香蕉，然后这一小时内不会再吃更多的香蕉。
#珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
#返回她可以在h小时内吃掉所有香蕉的最小速度k（k为整数）。

#输入：piles=[3,6,7,11]，h=8 输出：4

#输入：piles=[30,11,23,4,20]，h=5 输出：30

def min_eating_speed(piles, h):
    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        hours_needed = sum((pile + mid - 1) // mid for pile in piles) #以速度mid吃香蕉，计算需要的时间

        if hours_needed <= h:
            right = mid #在规定时间内吃完，减小速度
        else:
            left = mid + 1 #需要更多时间，增大速度

    return left

piles1 = [3, 6, 7, 11]
h1 = 8
result1 = min_eating_speed(piles1, h1)
print(result1)  # 输出: 4

piles2 = [30, 11, 23, 4, 20]
h2 = 5
result2 = min_eating_speed(piles2, h2)
print(result2)  # 输出: 30
