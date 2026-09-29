"""
- 链表中第一个存储数据的结点称为首元结点，一般在首元结点之前附加一个结点称为头结点。添加头结点有以下好处
    1. 由于第一个数据结点的位置被存放在头结点的指针域中，因此链表的第一个位置操作和其他位置操作一样，无需特殊处理
    2. 无论链表是否为空，其头指针都指向一个结点，这样空表和非空表的操作就实现了统一
"""

class LNode:
    """
    单链表节点类，包含数据元素和指向下一个节点的指针
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    单链表类，带头节点
    """

    def __init__(self):
        # 头节点
        self.head = LNode(None)
        self.length = 0

    def append(self, data):
        # 在链表尾插入元素  O(N)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = LNode(data)
        self.length += 1

    def get(self, index):
        # index=0代表头节点 O(N)
        if index <= 0 or index > self.length:
            return None

        cur_i = 0
        cur_node = self.head
        while cur_node is not None and cur_i < index:
            cur_node = cur_node.next
            cur_i += 1

        return cur_node.data

    def insert(self, index, data):
        if index <= 0 or index > self.length + 1:
            raise IndexError(f"index out of range, index should be in [1, {self.length+1}]")
        cur_i = 0
        cur_node = self.head
        while cur_node is not None and cur_i < index - 1:
            cur_node = cur_node.next
            cur_i += 1

        cur_node_next_tmp = cur_node.next
        cur_node.next = LNode(data, next=cur_node_next_tmp)
        self.length += 1

    def delete(self, index):
        if index <= 0 or index > self.length:
            raise IndexError(f"index out of range, index should be in [1, {self.length}]")
        cur_i = 0
        cur_node = self.head
        while cur_node is not None and cur_i < index - 1:
            cur_node = cur_node.next
            cur_i += 1

        cur_node_next_tmp = cur_node.next
        cur_node.next = cur_node_next_tmp.next
        self.length -= 1

    def __str__(self):
        print_str = f"[Linked List]: "
        if self.head.next is not None:
            print_str += 'head -> '
        else:
            print_str += 'head'

        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_node.next is not None:
                print_str += f'{cur_node.data} -> '
            else:
                print_str += f'{cur_node.data}'
        return print_str

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    ll = LinkedList()
    for i in [1, 9, 2, 8, 3, 7, 4, 6, 5]:
        ll.append(i)
    print(ll)
    print(f'get 4: {ll.get(4)}')
    ll.insert(4, 10)
    print(f'insert (4,10): {ll}')
    ll.delete(4)
    print(f'delete 4: {ll}')