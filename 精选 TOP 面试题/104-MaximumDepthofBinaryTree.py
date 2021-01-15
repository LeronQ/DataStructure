

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
        def top_down(node,h):
            return h if node is None else max(top_down(node.left,h+1),top_down(node.right,h+1))
        return top_down(root,0)