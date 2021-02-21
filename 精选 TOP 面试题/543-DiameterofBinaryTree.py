


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def maxDiameter(root):
            nonlocal res
            if not root:
                return 0
            
            l = maxDiameter(root.left)
            r = maxDiameter(root.right)
            res = max(res, l + r)
            return max(l, r) + 1
        
        maxDiameter(root)
        return res