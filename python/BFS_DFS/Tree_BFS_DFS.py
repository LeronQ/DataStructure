class TreeNode:

    def __init__(self, value):
        self._value       = value
        self._parent_node = None
        self._left_node   = None
        self._right_node  = None

    def get_right_branch(self):
        return self._right_node

    def get_left_branch(self):
        return self._left_node

    def get_parent_branch(self):
        return self._parent_node

    def set_right_branch(self, node):
        self._right_node = node

    def set_left_branch(self, node):
        self._left_node = node

    def set_parent_branch(self, node):
        self._parent_node = node

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def __str__(self):
        return "Node Value: {}".format(self._value)

def create_binary_tree():
    #
    #           n5
    #          /  \
    #         n2   n8
    #        / \   /
    #       n1 n4 n6
    #               \
    #               n7
    #
    n5 = TreeNode(5)
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    n4 = TreeNode(4)
    n8 = TreeNode(8)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n5.set_left_branch(n2)
    n2.set_parent_branch(n5)
    n5.set_right_branch(n8)
    n8.set_parent_branch(n5)
    n2.set_left_branch(n1)
    n1.set_parent_branch(n2)
    n2.set_right_branch(n4)
    n4.set_parent_branch(n2)
    n8.set_left_branch(n6)
    n6.set_parent_branch(n8)
    n6.set_right_branch(n7)
    n7.set_parent_branch(n6)
    return n5


def DFS_binary(root, fcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
    return False

def BFS_binary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
    return False

# trace path
def DFS_binary_path(root, fcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return trace_path(stack[0])
        else:
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
    return False

def trace_path(node):
    if not node.get_parent_branch():
        return [node]
    else:
        return trace_path(node.get_parent_branch()) + [node]

def find6(node):
    print("at node : {}".format(node.get_value()))
    return node.get_value() == 6

def find10(node):
    print("at node : {}".format(node.get_value()))
    return node.get_value() == 10

if __name__ == "__main__":
    root = create_binary_tree()
    print("####### DFS #######")
    DFS_binary(root, find6)
    print("-----------------")
    DFS_binary(root, find10)
    print("####### BFS #######")
    BFS_binary(root, find6)
    print("-----------------")
    BFS_binary(root, find10)
    print("#### DFS - Path ####")
    pathto_6_list = DFS_binary_path(root, find6)
    print("root -> goal")
    for e in pathto_6_list:
        print(e.get_value(), end = " ")