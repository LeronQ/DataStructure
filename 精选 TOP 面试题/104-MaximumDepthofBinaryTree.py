

# 104. Maximum Depth of Binary Tree
# 二叉树最大深度，递归求解

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        l = self.maxDepth(root.left)+1
        r = self.maxDepth(root.right)+1
        return max(l,r)