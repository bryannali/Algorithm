#有4张分别写有1到9数字之一的牌，需要判断是否能通过×、/、+、-、(，)的运算得到24。

#输入：[4,1,8,7] 输出：True 解释：(8-4)×(7-1)=24。

#输入：[1,2,1,2] 输出：False

def judgePoint24(nums):
    EPSILON = 1e-6  # 用于处理浮点数精度问题

    def dfs(nums):
        if len(nums) == 1:
            # 如果剩下一个数字，判断是否等于24（考虑浮点数精度问题）
            return abs(nums[0] - 24) < EPSILON

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    #不包含第i和第j个元素
                    new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                    #加法
                    if j > i:
                        new_nums.append(nums[i] + nums[j])
                        if dfs(new_nums):
                            return True
                        new_nums.pop()

                    #减法
                    new_nums.append(nums[i] - nums[j])
                    if dfs(new_nums):
                        return True
                    new_nums.pop()

                    #乘法
                    if j > i:
                        new_nums.append(nums[i] * nums[j])
                        if dfs(new_nums):
                            return True
                        new_nums.pop()

                    #除法
                    if nums[j] != 0:
                        new_nums.append(nums[i] / nums[j])
                        if dfs(new_nums):
                            return True
                        new_nums.pop()
        return False
    return dfs(nums)

print(judgePoint24([4, 1, 8, 7]))  
print(judgePoint24([1, 2, 1, 2]))  
