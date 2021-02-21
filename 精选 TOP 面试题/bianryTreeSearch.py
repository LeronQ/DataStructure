
# 二叉树前、中、后遍历

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前序遍历-递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(root):
            nonlocal res
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res

# 前序遍历-迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

# 中序遍历-递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            nonlocal res
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

# 中序遍历-迭代
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


# 后序遍历-递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(root):
            nonlocal res
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res

# 后序遍历-迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left :
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]




# 二叉树层次遍历

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 层次遍历
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


# 二叉树深度
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        lDepth = self.TreeDepth(pRoot.left)
        rDepth = self.TreeDepth(pRoot.right)
        return max(lDepth,rDepth)+1