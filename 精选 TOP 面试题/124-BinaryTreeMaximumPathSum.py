
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        def helper(node):
            nonlocal ans
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            ans = max(ans, max(l,0) + max(r, 0) + node.val)
            return max(l, r, 0) + node.val
        helper(root)
        return ans