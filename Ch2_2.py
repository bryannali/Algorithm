#给定一个包含n个整数的数组nums，判断nums中是否存在3个元素a、b、c，使a+b+c=0。
# 找出所有满足条件且不重复的三元组。

#注意：答案中不可以包含重复的三元组。
#例如，给定数组 nums=[-1,0,1,2,-1,-4]，满足要求的三元组集合为[[-1,0,1]，[-1,-1,2]]。

nums=[-1,0,1,2,-1,-4]
def solution1(nums):
    n = len(nums)
    nums.sort()
    res = []

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]: 
            continue
        l = i + 1
        r = n - 1
        while(l < r):
            if(nums[i] + nums[l] + nums[r] < 0):
                l += 1
            elif(nums[i] + nums[l] + nums[r] > 0):
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while(l < r and nums[l] == nums[l+1]): 
                    l += 1
                while (l < r and nums[r] == nums[r-1]):
                    r -= 1
                l += 1
                r -= 1
    return res
result1 = solution1(nums)
print("方法1：" + str(result1))





#第二天自己做第二遍
#给出数组nums[-4， -2， 2， 4， 4， 0]，找出所有并且不重复的三个数字相加为0，返回列表形式
nums = [-4, -4, -2, 2, 4, 4, 0]
def solution2(nums):
    n = len(nums)
    nums.sort()
    lis = []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]: #跳过相邻重复的元素
            continue #直接跳过 进入到下一个for循环语句
        l = i + 1
        r = n - 1
        while(l < r):
            if(nums[i] + nums[l] + nums[r] < 0):
                l += 1
            elif(nums[i] + nums[l] + nums[r] > 0):
                r -= 1
            else:
                lis.append([nums[i], nums[l], nums[r]])
                while(l < r and nums[l] == nums[l+1]): #在找到list之后 继续判断有没有相邻重复元素
                    l += 1
                while (l < r and nums[r] == nums[r-1]):
                    r -= 1
                l += 1
                r -= 1
    return lis
result1 = solution2(nums)
print("方法2：" + str(result1))
