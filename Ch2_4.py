#给定4个包含整数的数组列表A、B、C、D，计算有多少个元组(i,j,k,l)能使A[i]+B[j]+C[k]+D[l]=0。
#为了使问题简单化，所有的A、B、C、D具有相同的长度n，且0≤n≤500。所有整数的范围在-228到228-1之间，最终结果不会超过231-1。

#输入：A=[1,2]，B=[-2,-1]，C=[-1,2]，D=[0,2]
#输出：2

#解释：两个元组如下。
#(0,0,0,1)→A[0]+B[0]+C[0]+D[1]=1+(-2)+(-1)+2=0
#(1,1,0,0)→A[1]+B[1]+C[0]+D[0]=2+(-1)+(-1)+0=0

A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]

def fourSumCount(A, B, C, D):
    sum_count = {}

    for a in A:
        for b in B: #遍历A和B，把所有的和存在字典中
            if (a + b) in sum_count:
                sum_count[a + b] += 1
            else:
                sum_count[a + b] = 1
    result = 0

    for c in C:
        for d in D: #遍历C和D，查找相反数
            if -(c + d) in sum_count: #如何相反，则+1
                result += sum_count[-(c + d)]
    return result

print(fourSumCount(A, B, C, D)) 
