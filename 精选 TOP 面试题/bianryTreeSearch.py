
# 二叉树前、中、后遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #前序
    def preorder(self,root,ans=[]):
        if root!=None:
            ans.append(root.val)
        if root.left:
            self.preorder(root.left,ans)
        if root.right:
            self.preorder(root.right,ans)
        return ans
    
    #中序
    def inorder(self,root,ans=[]):
        # if root.left==None and root.right==None:
        #     ans.append(root.val)
        #     return
        if root.left:
            self.inorder(root.left,ans)
        ans.append(root.val)
        if root.right:
            self.inorder(root.right,ans)
        return ans
    
    #后序
    def postorder(self,root,ans=[]):
        if root.left:
            self.postorder(root.left,ans)
        if root.right:
            self.postorder(root.right,ans)
        ans.append(root.val)
        return ans




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