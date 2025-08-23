class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head  # 接受外部构建的头节点
    
    # 查询链表的长度
    def length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length
    
    # 获取指定索引的节点
    def get_node_at_index(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        
        current = self.head
        current_index = 0
        
        while current:
            if current_index == index:
                return current
            current = current.next
            current_index += 1
        
        raise IndexError("Index out of range")
    
    # 打印链表
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# 独立函数：根据列表构建链表
def build_from_list(data_list):
    if not data_list:
        return None
    
    head = ListNode(data_list[0])  # 创建头节点
    current = head
    
    for value in data_list[1:]:
        new_node = ListNode(value)
        current.next = new_node  # 将当前节点的next指向新节点
        current = new_node  # 移动到新节点
    
    return head

# 测试
data = [1, 2, 3, 4]

# 使用独立函数构建链表
head = build_from_list(data)

# 将构建好的链表传递给 LinkedList
linked_list = LinkedList(head)
linked_list.print_list()  # 打印链表
print("链表的长度:", linked_list.length())  # 查询链表长度

# 获取索引为2的节点
index = 2
node = linked_list.get_node_at_index(index)
print(f"索引 {index} 的节点值:", node.value)
