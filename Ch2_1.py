# 给定一个整数数组nums和一个目标值target，
# 请你在该数组中找出和为目标值的那两个整数，并返回它们的索引值。
# 你可以假设每种输入只会对应一个答案，但是，你不能重复利用这个数组中同样的元素。

#给定 nums=[2,7,11,15]，target=9
#因为 nums[0]+nums[1]=2+7=9，所以返回[0,1]

nums=[2,11,15,7]
target=9

#毫无逻辑 最笨的方法 (两层循环 一个一个遍历)：

def solution1(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
result1 = solution1(nums, target)
print("笨蛋方法1：" + str(result1))

#方法2 先排序，取首尾元素相加。循环 如果目标值大于结果值 尾元素-1，反之 首元素+1:
def solution2(nums, target):
    new_nums = nums.sort()
    x = 0
    y = len(new_nums)-1
    while True:
        if x + y > target:
            y -= 1
        elif x + y < target:
            x += 1
        else:
            # x = x
            # y = y
            break
    index1 = nums.index(new_nums[x])
    index2 = nums.index(new_nums[y])
    return [index1, index2]
result2 = solution1(nums, target)
print("方法二：" + str(result2))

#方法3 哈希表遍历
def solution3(nums, target):
    n = len(nums)
    mapper = {}
    for i in range(n):
        if (target - nums[i] in mapper):
            return [mapper[target - nums[i]], i] #[mapper里寻找被减值的索引，当前值的索引]
        else:
            mapper[nums[i]] = i
    return []
result3 = solution3(nums, target)
print("方法三：" + str(result3))