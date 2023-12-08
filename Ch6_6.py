#给定一个非负整数数组和一个整数m，你需要将这个数组分成m个非空的连续子数组。设计一个算法使这m个子数组各自和的最大值最小。
#注意：数组长度n满足以下条件。
# 1≤n≤1000。
# 1≤m≤min(50,n)。
#输入：nums=[7,2,5,10,8]，m=2 输出：18

def split_array(nums, m):
    def count_groups(mid):
        # 以mid为上限值时，需要分成的子数组个数
        groups = 1
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum > mid:
                groups += 1
                current_sum = num

        return groups

    left, right = max(nums), sum(nums)

    while left < right:
        mid = left + (right - left) // 2
        # 计算以mid为上限值时，需要分成的子数组个数
        groups = count_groups(mid)

        if groups > m:
            # 如果需要的子数组个数大于m，说明mid太小，增大mid
            left = mid + 1
        else:
            # 如果需要的子数组个数小于等于m，说明mid足够大，缩小mid
            right = mid
    return left

nums = [7, 2, 5, 10, 8]
m = 2
result = split_array(nums, m)
print(result)  # 输出: 18
