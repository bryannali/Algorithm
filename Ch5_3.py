#给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#示例：给定如下二叉树，以及目标和sum=22。返回True，因为存在目标和为22的根节点到叶子节点的路径5→4→11→2。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if not root:
        return False
 
    if not root.left and not root.right:
        return targetSum == root.val

    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

#     5
#    / \
#   4   8
#  /   / \
# 11  13  4
# /  \      \
# 7   2      1
root = TreeNode(5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
               )

print(hasPathSum(root, 22)) 
