
# 102：Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

# [
#   [3],
#   [9,20],
#   [15,7]
#  ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        flag = [root]
        while flag:
            ans = []
            for curr in flag:
                if curr.left:
                    ans.append(curr.left)
                if curr.right:
                    ans.append(curr.right)
            if ans:
                res.append([i.val for i in ans])
            flag = ans
        return res