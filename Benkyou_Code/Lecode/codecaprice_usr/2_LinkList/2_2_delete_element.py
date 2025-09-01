

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        # print(f"self is\n{self}")
    print

class Solution(object):
    def removeElements(self, head, val):
        pre = ListNode(0)
        pre.next = head
        temp = pre
        while temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return pre.next

def get_linklist(head):
    '''
    遍历单链表的元素
    '''
    if head == None:
        return head
    temp = head
    res = []
    while temp != None:
        res.append(temp.val)
        temp = temp.next
    return res

def create_linklist(array):
    '''
    构造单链表
    '''
    if not array:
        return None
    preNode = ListNode()
    pre = preNode
    for value in array:
        current = ListNode(value)
        pre.next = current # 注意此时 pre 和 preNode 同步更改
        pre = current # 此时仅有 pre 更改为 current
        '''
        pre.next = current 会修改 preNode 的 next 指向
        而 pre = current 只是让 pre 指向 current ，并不会影响 preNode
        '''
        # print(f"pre is\n{pre}")
        # print(f"preNode is\n{preNode}")
        print
    # print(f"preNode is\n{preNode}")
    get_linklist(preNode.next)
    print

    return preNode.next

def main():
    head = [1, 2, 3, 4, 5, 6]
    val = 5
    head = create_linklist(head)
    # print(head)
    solution = Solution()
    head = solution.removeElements(head, val)
    get_linklist(head)
    print(f"head:\n{head}")
    print

if __name__=="__main__":
    main()