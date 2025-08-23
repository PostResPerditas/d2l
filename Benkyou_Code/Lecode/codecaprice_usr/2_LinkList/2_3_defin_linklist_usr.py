
# 初始化链表
class ListNode(object):

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def build_from_list(data_list):

    if not data_list:
        print('there is no input data list')
        return None
    
    # 构建链表头节点
    head = ListNode(data_list[0])
    current = head

    # 迭代导入链表后续节点
    for value in data_list[1:]:
        # 需要使用 new_data 新建一个实例
        new_data = ListNode(value)
        current.next =new_data
        current = new_data

#     # 错误写法，迭代导入链表后续节点
#     for value in data_list[1:]:
#         '''
#         每次循环中 current 被覆盖为一个新的孤立节点。
#         最后链表会断开，只有第一个循环中的节点正确连接，其余节点丢失。
#         '''
#         current.next =ListNode(value)
#         current = ListNode(value)

    return head

class LinkedList(object):
    def __init__(self, head=None):
        # 对 self 进行添加 head 项目(默认为 None)
        self.head = head # 允许外界输入 head

    def get_len(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next

        return length
    
    def get_index_element(self, index):
        length = LinkedList.get_len(self)
        # print(f"length is\n{length}")
        if index >= length:
            return -1 # 超出索引范围
        elif index < 0:
            return -1
        current = self.head
        current_index = 0

        for _ in range(index):
            current = current.next
            current_index += 1

        return current.value
        
    def addAtHead(self, value):
        # 初始化新加入的链表值
        currentNode = ListNode(value)
        # # 将原有链表向后移动
        # head = self.head
        # # 将移动后的原列表添加到新列表中
        # currentNode.next = head
        currentNode.next = self.head
        print
        return currentNode

    def addAtTail(self, value):
        currentNode = ListNode(value)
        head = self.head
        while head.next != None:
            head = head.next
        head.next = currentNode

        return self.head

    def addAtIndex(self, index, value):
        insertNode = ListNode(value)
        # 注意使用 next 实现的 current 修改会同步到 head 上
        current = self.head
        for _ in range(index):
            current = current.next
        insertNode.next = current.next
        current.next = insertNode # 由于 current 和 self.head 有相同的结构(.next)，且 current 指向 self.head，因此进行 .next 赋值会同步修改 self.head

        return self.head


def main():
    # 测试
    data = [1, 2, 3, 4]

    # 使用独立函数构建链表
    head = build_from_list(data)
    # print(f"head is\n{head}")

    linked_list = LinkedList(head)
    # length = linked_list.get_len()
    # print(f"length is\n{length}")

    node = linked_list.get_index_element(1)
    # print(f"node is\n{node}")

    # head_addh = linked_list.addAtHead(1)

    # head_addt = linked_list.addAtTail(1)

    head_addi = linked_list.addAtIndex(0,1)
    print

if __name__=="__main__":
    main()
    print