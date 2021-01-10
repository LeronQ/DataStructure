


#141. Linked List Cycle

# 检测单链表是否存在环

# method 1： 用一个集合存储遍历的节点，如果已经出现，则表示存在环

# 优点：容易理解
# 缺点：用到新的存储空间

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 用一个集合来表示遍历的节点信息，如果重复出现，则表明存在环
        seen = set()
        cur = head
        while cur is not None:
            if cur in seen:
                return True
            else:
                seen.add(cur)
                cur = cur.next
        return False



# method 2： # 用两个快慢指针，如果在某个节点相遇，则表示存在环

# 优点：没有新的存储空间，运行更加高效

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 用两个快慢指针，如果在某个节点相遇，则表示存在环
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

