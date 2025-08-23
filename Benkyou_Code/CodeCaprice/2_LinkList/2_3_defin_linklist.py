"""
题目: 707. 设计链表
链接: https://leetcode.cn/problems/design-linked-list/description/
思路:
    1. 初始化pre节点和链表长度len
    2. 对于get, deleteatIndex， addatIndex 首先判断索引是否符合规则 不符合直接返回None或者是-1 遍历到index前一个节点即可
    3. 头插法和尾插入法
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.pre = ListNode(0)
        self.len = 0

    # 得到链表的长度
    def get_len(self, pre):
        temp = self.pre.next
        len = 0
        while temp != None:
            temp = temp.next
            len += 1
        return len

    # 得到index索引的节点
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.len:
            return -1
        temp = self.pre.next
        for i in range(index):
            temp = temp.next
        return temp.val

    # 头插法
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        currentNode = ListNode(val)
        head = self.pre.next
        currentNode.next = head
        self.pre.next = currentNode
        self.len += 1


    # 尾插法
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        tail = self.pre
        tailNode = ListNode(val)
        while tail.next != None:
            tail = tail.next
        tail.next = tailNode
        self.len += 1

    # val插入到index
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.len:
            return None
        temp = self.pre
        for i in range(index):
            temp = temp.next
        valNode = ListNode(val)
        valNode.next = temp.next
        temp.next = valNode
        self.len += 1


    # 删除index位置的节点
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.len:
            return None
        temp = self.pre
        for i in range(index):
            temp = temp.next
        temp.next = temp.next.next

        self.len -= 1

if __name__ == '__main__':
    print("hello solution")
