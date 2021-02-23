

class Node(object):
    def __init__(self,x,y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hkeys = {}
        self.top = Node(None,-1)
        self.tail = Node(None,-1)
        self.top.next = self.tail
        self.tail.prev = self.top
    def get(self, key: int) -> int:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            # 跳出原来位置
            cur.next.prev = cur.prev
            cur.prev.next = cur.next

            top_node  = self.top.next
            self.top.next = cur 
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur 
            return self.hkeys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            # 跳出原位置
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            cur = Node(key,value)
            self.hkeys[key] = cur 
            #增加新节点至首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            if len(self.hkeys.keys())>self.capacity:
                # 去掉map中的key
                self.hkeys.pop(self.tail.prev.key)
                # 去掉尾节点
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
