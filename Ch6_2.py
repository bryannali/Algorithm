#假设按照升序排序的数组在预先未知的某个点上进行了旋转
# （例如数组[0,1,2,4,5,6,7]可能变为[4,5,6,7,0,1,2]），
# 请找出其中最小的元素。你可以假设数组中不存在重复元素。

#输入：[3,4,5,1,2] 输出：1
#输入：[4,5,6,7,0,1,2] 输出：0
def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1 #最小元素在右侧
        else:
            right = mid #最小元素在左侧或当前位置

    return nums[left]

nums1 = [3, 4, 5, 1, 2]
result1 = find_min(nums1)
print(result1)  # 输出: 1

nums2 = [4, 5, 6, 7, 0, 1, 2]
result2 = find_min(nums2)
print(result2)  # 输出: 0
