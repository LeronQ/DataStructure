# -*- coding: utf-8 -*-
# @Author : Lv
# @File : linklist.py


'''
    单链表的节点插入，更新，删除，去重和反转等操作
'''


class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Lianbiao(object):
    """docstring for Lianbiao"""

    def __init__(self):
        self.root = None

    def addNode(self, data):
        '''
            向单链表增加节点
        '''
        # 如果没有根节点
        if self.root == None:
            self.root = Node(data=data, next=None)
            return self.root
        else:
            # 如果已经有根节点
            cursor = self.root
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = Node(data=data, next=None)
            return self.root

    # 在链表尾部增加新的节点，调用底层addNode方法
    def append(self, value):
        self.addNode(data=value)

    # 在链表首部添加节点
    def prepend(self, value):
        if self.root == None:
            self.root = Node(value, None)
        else:
            newroot = Node(value, None)
            # 更新root索引
            newroot.next = self.root
            self.root = newroot

    # 在链表指定位置添加节点
    def insert(self, index, value):
        if self.root == None:
            return
        if index <= 0 or index > self.size():
            print('index %d 非法，审视一插入节点在整个链表的位置！')
            return
        elif index == 0:
            # 如果index=1，则在链表首部添加即可
            self.prepend(value)
        else:
            # 在链表中间添加元素，使用计数器来维护插入位置
            counter = 1
            pre = self.root
            cursor = self.root.next
            while cursor != None:
                # 判断是否在头结点的后面插入
                # 1:如果是在头结点的后面插入
                if counter == index:
                    temp = Node(value, None)
                    pre.next = temp
                    temp.next = cursor
                    break
                else:
                    # 2:如果是在中间节点插入
                    counter += 1
                    pre = cursor
                    cursor = cursor.next

    # 删除指定位置上的节点
    def delNode(self, index):
        if self.root == None:
            return
        if index < 0 or index > self.size():
            print('index %d 非法，审视一下插入节点在整个链表的位置！')
            return
        if index == 0:  # 如果删除的是首节点
            self.root = self.root.next
        else:
            pre = self.root
            cursor = self.root.next
            counter = 1
            while cursor != None:
                if index == counter:
                    pre.next = cursor.next
                    break
                else:
                    pre = cursor
                    cursor = cursor.next
                    counter += 1

    # 删除值为value的链表节点元素
    def delValue(self, value):
        if self.root == None:
            return
        # 如果要删除的是首节点对应的值
        if self.root.data == value:
            self.root = self.root.next
        else:
            pre = self.root
            cursor = self.root.next
            while cursor != None:
                if cursor.data == value:
                    pre.next = cursor.next
                    # 一定要更新这个节点，否则会死循环
                    cursor = cursor.next
                    continue
                else:
                    pre = cursor
                    cursor = cursor.next

    # 判断链表是否为空
    def isEmpty(self):
        if self.root == None or self.size() == 0:
            return True
        else:
            return False

    # 删除链表及其内部所有元素
    def truncate(self):
        if self.root == None or self.size() == 0:
            return
        else:
            cursor = self.root
            while cursor != None:
                cursor.data = None
                cursor = cursor.next
            self.root = None
            cursor = None

    # 获取指定位置的节点的值-- 按实际位置顺序，不是索引
    def getvalue(self, index):
        if self.root is None or self.size() == 0:
            print('当前链表为空')
            return None
        if index <= 0 or index > self.size():
            print("index %d不合规！" % index)
            return None
        else:
            counter = 1
            cursor = self.root
            while cursor != None:
                if index == counter:
                    return cursor.data
                else:
                    counter += 1
                    cursor = cursor.next

    # 删除链表中的重复元素
    def delDuplecate(self):
        # 使用一个map来存放即可，类似于变形的“桶排序”
        if self.root == None:
            return
        if self.size() == 1:
            return
        pre = self.root
        cursor = self.root.next
        dic = {}

        # 给字典赋值
        temp = self.root
        while temp != None:
            dic[str(temp.data)] = 0
            temp = temp.next

        # 然后进行删除重复元素操作
        while cursor != None:
            if dic[str(cursor.data)] == 0:
                # 在字典中首次出现的标记值加1，如果该值出现次数大于1，则标记值也会大于1
                dic[str(cursor.data)] += 1
                pre = cursor
                cursor = cursor.next
            else:
                pre.next = cursor.next
                cursor = cursor.next

    # 单链表反转
    def reverse(self):
        # 单链表逆序实现
        if self.root == None:
            return
        if self.size() == 1:
            return
        else:
            pre = None
            cursor = self.root
            while cursor != None:
                post = cursor.next
                cursor.next = pre
                pre = cursor
                cursor = post
            self.root = pre

    # 修改指定位置节点的值
    def updateNode(self, index, value):
        if self.root == None:
            return
        if index < 0 or index > self.size():
            return
        if index == 0:
            self.root.data = value
        else:
            cursor = self.root.next
            counter = 1
            while cursor != None:
                if counter == index:
                    cursor.data = value
                    break
                cursor = cursor.next
                counter += 1

    # 获取单链表的大小
    def size(self):
        counter = 0
        if self.root == None:
            return counter
        else:
            cursor = self.root
            while cursor != None:
                counter += 1
                cursor = cursor.next
            return counter

    # 打印链表自身元素
    def print(self):
        if (self.root == None):
            return
        else:
            cursor = self.root
            while cursor != None:
                print(cursor.data, end='\t')
                cursor = cursor.next
                pass

    # 判断是否是回文链表
    def is_palindrome(self):
        if self.root == None:
            return False
        if self.size() == 1:
            return True
        slow = fast = self.root
        
        # 1:定位中点
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        '''快慢指针定位中点，此时fast已到达链尾
        如果长度为奇数，则slow到达中心点，长度为偶数，则slow到达下中位点
        '''
        
         # 2:后半段倒置
        pre = None 
        cur = slow
        nxt = slow.next
        
        while nxt:
            cur.next = pre # 将当前节点的下一个节点指向"前"一个节点，进行倒置
            pre = cur
            cur = nxt
            nxt = cur.next
            
        # 当前cur是最后一个节点，需要和它前面的节点进行最后一次倒置，来完成整个后半段倒置
        cur.next = pre 
        
        # 3.ur就是倒置完成后的后半段的头节点,同时遍历cur和head，如果遍历完cur未出现不同的节点，则为回文链表
        while cur.next != None:
            if cur.data != self.root.data:
                return False
            cur = cur.next
            self.root = self.root.next
        return True
        
        
        

if __name__ == '__main__':
    # 创建一个链表对象
    lianbiao = Lianbiao()
    # 判断当前链表是否为空
    lianbiao.addNode(2)
    # 添加一些节点，方便操作
    lianbiao.addNode(4)
    lianbiao.addNode(6)
    lianbiao.addNode(6)
    lianbiao.addNode(4)
    lianbiao.addNode(2)
    # 打印当前链表所有值
#    print('打印当前链表所有值:',end="\n")
#    lianbiao.print()
#    print('\n')
#
#    # 链表的大小
#    print("链表的size: " + str(lianbiao.size()))
#    # 链表的插入，并打印插入后的结果
#    lianbiao.insert(1, 4)
#    lianbiao.print()
#    print('\n')
#    # 链表指定位置值的获取
#    print("链表指定位置值的获取:"+ str(lianbiao.getvalue(1)))
#
#    # 链表指定位置删除值
#    #lianbiao.delValue(3)
#    
#    print("更新链表指定位置数值：")
#    # 更新链表指定位置的数值
#    lianbiao.updateNode(6, 2)
#    lianbiao.print()
#    print('\n')

#    print("去除重复元素：")
#    lianbiao.delDuplecate()
#    lianbiao.print()
    
    # 判断是否是回文链表
    print('\n')
    print("判断是否是回文链表：")
    print(lianbiao.is_palindrome())

