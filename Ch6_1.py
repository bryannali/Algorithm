#给定一个有n个元素的、有序的（升序）整型数组nums和一个目标值target，
# 写一个函数搜索nums中的target，如果目标值存在，则返回其下标，否则返回-1。

#输入：nums=[-1,0,3,5,9,12]，target=9 输出：4
#解释：9出现在nums中且下标为4。

#输入：nums=[-1,0,3,5,9,12]，target=2 输出：-1
#解释：2不存在于nums中，因此返回-1。
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
result1 = search(nums1, target1)
print(result1)  # 输出: 4

nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
result2 = search(nums2, target2)
print(result2)  # 输出: -1
