#峰值元素是指其值大于左右相邻值的元素。
# 给定一个输入数组nums，其中nums[i]≠ nums[i+1]，找到峰值元素并返回其索引值。
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在的位置即可。
# 你可以假设nums[-1]=nums[n]=-∞。

#输入：nums=[1,2,3,1] 输出：2 解释：3是峰值元素，函数应该返回其索引值2。

#输入：nums=[1,2,1,3,5,6,4] 输出：1或5 解释：函数可以返回索引值1，其峰值元素为2；或者返回索引值5，其峰值元素为6。

def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        #如果中间元素比右边元素大，那么峰值一定在左半部分
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            # 否则，峰值一定在右半部分
            left = mid + 1
    return left


nums1 = [1, 2, 3, 1]
result1 = find_peak_element(nums1)
print(result1)  # 输出: 2

nums2 = [1, 2, 1, 3, 5, 6, 4]
result2 = find_peak_element(nums2)
print(result2)  # 输出: 1 或 5
