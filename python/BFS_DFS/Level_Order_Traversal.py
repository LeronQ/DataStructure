


"""
    @author: lv
"""


''' 
要求1：
    给定一棵二叉树,从上到下，每层从左到右打印
    适用于完全二叉树，满二叉树或者非满二叉树

解题思路：
可以借助BFS算法，利用队列（程序中，用数组代替）实现
    1：首先将root节点加入队列中
    2：队列不为空时，取出队首节点，然后将队首节点打印出来
    3：将打印的节点的左右子节点依次加入队尾（BFS算法）
    4：回到步骤2，直到队列为空


要求2：  -----leetcode 102：Binary Tree Level Order Traversal
    将每一层节点数据放在一个数组里，最后返回一个包含完整层次数据的数组


要求3：---- leetcode:129. Sum Root to Leaf Numbers
    从根节点到所有叶子节点的所有可能的路线，连接起来组成一个数据，然后求和---- 也就是有多少个叶子节点，累加多少个数据
'''


class TreeNode():
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

# 1：一行打印        
def one_line_print(root):
    '''一行内打印，不换行'''
    if not root:
        return 
    queue= []
    queue.append(root)
    while (len(queue) > 0):
        node = queue.pop(0)  # BFS的核心
        print(node.val,end = ' ') # 显示在一行，以空格作为分隔符
        if node.left:   # 逐层遍历
            queue.append(node.left) # 将左子节点加入队列中
        if node.right:
            queue.append(node.right) # 将右子节点加入队列中

# 2：逐行打印
def layer1_print(root):
    '''每层换行打印'''
    if not root:
        return
    queue =[]
    curLine  = 0
    queue.append([curLine,root])
    while(len(queue)>0):
        line,node = queue.pop(0)
        if line != curLine:
            print('\n')
            curLine = line
        print (node.val,end=' ')
        if node.left:
            queue.append([line+ 1,node.left]) # 将左子节点加入队列中
        if node.right:
            queue.append([line+ 1,node.right])# 将右子节点加入队列中

 
# 3:逐行打印--优化版
''' layer1_print 函数增加了line/current_line两个变量，并且node入队时，增加了额外的空间开销;

    解决办法，在每个左子节点入队之前，增加一个换行标记
'''
def layer2_print(root):
    '''每层换行打印'''
    if not root:
        return
    queue = ['next']
    queue.append(root)
    while (len(queue) > 0):
        node = queue.pop(0)
        if isinstance(node,TreeNode):
            print(node.val,end = ' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            # 条件
            if len(queue) > 0:
                queue.append('next')
                print('\n')
    
def levelOrder(root):
    res = []
    preorder(res, 0, root)
    return res

def preorder(res, level, root):
    if root:
        if len(res) < level + 1:
            res.append([])

        res[level].append(root.val)

        preorder(res, level + 1, root.left)
        preorder(res, level + 1, root.right)   
    

def sumNumbers1(root):
    if not root:
        return 0
    stack, res = [(root, root.val)], 0
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right:
                res += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
    return res
    
if __name__ == "__main__":
    # 新建节点
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    
    # 创建二叉树
    node1.left = node2
    node1.right = node3
    
    node2.left = node4
    node2.right = node5
    
    node3.left = node6
    node3.right = node7
    
    node4.left = node8
    node4.right = node9
    
    node5.left = node10
    
    # 指定根节点
    root = node1
    
    # 打印在一行
    one_line_print(root)
    
    print('\n')
    # 逐行打印
    layer1_print(root)
    
    print('\n')
    # 逐行打印  -- 优化后
    layer2_print(root)

    print('\n')
    result=levelOrder(root)
    print(result)

    print('\n')
    res=sumNumbers1(root)
    print(res)
