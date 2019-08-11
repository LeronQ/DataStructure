# @Time : 2019/8/11 
# @Author : Lv
# @File : binary_search_tree.py


from queue import Queue
import math


class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree():
    def __init__(self, val_list=[]):
        self.root =None
        for n in val_list:  # 插入数据
            self.insert(n)

    def insert(self,data):
        '''
        :param data: 插入的数据
        :return:
        '''
        assert(isinstance(data,int))

        if self.root is None:
            self.root = TreeNode(data) # 如果没有根节点，则将第一个插入的数据作为根节点
        else:
            n = self.root  # 取出根节点
            while n:
                p = n
                if data < n.val: # 如果插入的数，小于根节点，则作为左子节点，否则作为右子节点
                    n = n.left
                else:
                    n = n.right

            new_node = TreeNode(data)  # 新数据作为一个新的节点
            new_node.parent = p

            if data < p.val:
                p.left = new_node
            else:
                p.right = new_node

        return True


    def search(self,data):
        '''
        搜索，返回bst中的所有值为data节点列表
        :param data:
        :return:
        '''
        assert(isinstance(data,int))

        # 所有搜索到的节点
        res =[]
        n = self.root

        while n:
            if data < n.val:
                n = n.left
            else:
                if data == n.val:
                    res.append(n)
                n = n.right
        return res

    def delete(self,data):
        '''
        删除数据对应的节点
        :param data:
        :return:
        '''
        assert (isinstance(data, int))

        # 首先，search方法，先找到节点，再删除
        del_list = self.search(data)

        for n in del_list:
            # 父节点为空，又不是根节点，则已经不在树上，不用再删除
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)  # 调用删除节点的函数

    def _del(self,node):  # 传入参数是节点
        '''
        删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除N的父节点指针
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        :param node:
        :return:
        '''
        # 第一种情况
        if node.left is None and node.right is None:
            if node == self.root:
                self.root =None
            else:
                if node.val < node.parent.val:
                    node.parent.left = None
                else:
                    node.parent.right =None

                node.parent = None

        # 第二种情况,左子节点为空，右子节点不为空
        elif node.left is None and node.right is not None:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                node.right = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

            node.right.parent = node.parent
            node.parent = None
            node.right = None

        elif node.left is not None and node.right is None:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                node.left = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                node.left.parent = node.parent
                node.parent = None
                node.left = None

        # 第三种情况
        else:
            min_node = node.right
            # 找到右子树最小值节点
            if min_node.left:
                min_node = min_node.left
            if node.val != min_node.val:
                node.val = min_node.val
                self._del(min_node)

            # 右子树的最小值节点与被删除节点的值相等，再次删除原节点
            else:
                self._del(min_node)
                self._del(node)



    def get_min(self):
        """
        返回最小值节点
        :return:
        """
        if self.root is None:
            return None

        n = self.root
        while n.left:
            n = n.left
        return n.val

    def get_max(self):
        """
        返回最大值节点
        :return:
        """
        if self.root is None:
            return None

        n = self.root
        while n.right:
            n = n.right
        return n.val



