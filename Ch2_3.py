#给定一个包含n个整数的数组nums和一个目标值target，
#判断nums中是否存在4个元素a、b、c、d，使a+b+c+d的值与target相等

nums=[1,0,-1,0,-2,2]
target = 0

def fourSum(nums, target):
    nums.sort()
    results = []
    findNsum(nums, target, 4, [], results)
    return results

def findNsum(nums, target, N, tempList, results): #递归
    if len(nums) < N or N < 2:
        return

    if N == 2: #两数之和 用双指针方式找到两个元素
        l = 0
        r = len(nums) -1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(tempList + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[1-l]:
                    l += 1
                while r > l and nums[r] == nums[r+1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

    else: #N>2情况 (N-1)之和的递归调用
        for i in range(0, len(nums)):
            if i == 0 or i > 0 and nums[i-1] != nums[i]:
                findNsum(nums[i+1:], target - nums[i], N-1, tempList + [nums[i]], results)
    return

result1 = fourSum(nums, target)
print("方法1：" + str(result1))   