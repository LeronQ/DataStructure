# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def inorder(root):
    		if root == None:
    			return result
    		inorder(root.left)
    		result.append(root.val)
    		inorder(root.right)
    	inorder(root)
	return result