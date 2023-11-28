#给定一个非空二叉树，返回其最大路径和。
#本题中，路径被定义为一条从树中任意节点出发并达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#输入：[1,2,3] 输出：6

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')

    def max_path_sum_helper(node):
        nonlocal max_sum
        if not node:
            return 0

        #递归
        left_sum = max(max_path_sum_helper(node.left), 0)#计算左子树的最大路径和
        right_sum = max(max_path_sum_helper(node.right), 0)#计算右子树的最大路径和

        current_sum = node.val + left_sum + right_sum#计算包含当前节点的路径和

        max_sum = max(max_sum, current_sum)#更新

        return node.val + max(left_sum, right_sum)

    max_path_sum_helper(root)
    return max_sum
#    -10
#    / \
#   9  20
#      / \
#     15  7
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(maxPathSum(root))  #输出：42
