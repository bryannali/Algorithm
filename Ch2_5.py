#给定一个包括n个整数的数组nums和一个目标值target。
#找出nums中的3个整数，使它们的和与target最接近。
#返回这3个数的和。假定每组输入只存在唯一答案。

#例如，给定数组nums=[-1,2,1,-4]和target=1。
#与target最接近的3个数的和为2，即-1+2+1=2。

nums=[-1,2,1,-4]
target=1
def threeSumClosest(nums, target):
    nums.sort() 
    closest_sum = float('inf')  # 最接近的和为正无穷

    for i in range(len(nums) - 2):
        left = i + 1 #左边指针
        right = len(nums) - 1 #右边指针

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum #update和

            
            if current_sum < target:
                left += 1 #指针位置+1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum  # 如果找到和等于target，直接返回
    return closest_sum

result = threeSumClosest(nums, target)
print(result)
