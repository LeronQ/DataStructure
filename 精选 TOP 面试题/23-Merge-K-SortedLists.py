

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        all_nodes = []
        for node in lists:
            if node:
                # 遍历链表放入队列
                p = node
                while p:
                    all_nodes.append(p)
                    p = p.next
        all_nodes.sort(key=lambda x: x.val)

        dummyHead = ListNode()
        prev = dummyHead
        for node in all_nodes:
            prev.next = node
            prev = node
        return dummyHead.next