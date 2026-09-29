class ListNode:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre


class LRUCache:
    """
    LRUCache 的核心是最近最少使用的需要被删除，分析可知， LRU需要三种操作:
        1. get key: key在缓存中，需要将其优先级提升为最高，因为最近被使用
        2. put key: 缓存未满，将结点放到 cache 中，并且将其优先级提升为最高优先级
        3. put key: 缓存已满，删除优先级最低的 cache,再插入 key 为最高优先级

        cache 存储可以用哈希表实现，关键是如何记录优先级
        比较直观是可以使用线性表，一端表示最近使用过的，一段表示最近最少使用的，如何实现这个线性表？
        这个线性表需要满足什么操作？
            O(1) 时间在头部插入元素 (可以解决情况2)
            O(1) 时间删除尾部元素 (配合前者可以解决情况3)
            O(1) 时间更新一个元素的优先级，即 O(1) 时间查找一个元素 (这个只用链表无法实现)
        可以采用带头尾指针的双向链表+哈希表辅助：
            带头尾指针的双向链表 可以实现 O(1)时间在头尾插入
            加上哈希表的辅助可以在 O(1)时间找到一个结点
    """

    def __init__(self, capacity: int):
        self.capacity = capacity

        # 带头尾指针的双向链表，头尾分别添加一个结点用于统一操作
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

        # 哈希表辅助
        self.key2Node = {}

    # ---------- 工具函数 ----------
    def _add_to_head(self, node: ListNode):
        """
        O(1) 时间在头部插入
        """
        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node

    def _remove_node(self, node: ListNode):
        # O(1) 时间删除结点
        node.pre.next = node.next
        node.next.pre = node.pre

    def _move_to_head(self, node):
        """O(1)时间将结点移动到头部"""
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        """O(1)时间删除尾部结点"""
        node = self.tail.pre
        self._remove_node(node)
        return node

    # ---------- 核心操作 ----------
    def get(self, key: int) -> int:
        """
        如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1
        要求 O(1) 时间复杂度
        """
        if key in self.key2Node:
            node = self.key2Node[key]
            self._move_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        如果 关键字 key 已经存在，则变更其数据值 value
        如果不存在，则向缓存中插入该组 key-value,
        如果插入操作导致关键字数量超过 capacity, 则应该逐出最久未使用的关键字
        要求 O(1) 时间复杂度
        """
        if key in self.key2Node:
            node = self.key2Node[key]
            node.val = value
            self._move_to_head(node)
        else:
            new_node = ListNode(key, value)
            self.key2Node[key] = new_node
            self._add_to_head(new_node)
            if len(self.key2Node) > self.capacity:
                # 在尾部删除
                removed = self._remove_tail()
                del self.key2Node[removed.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def construct_linked_list(array) -> ListNode | None:
    if not array: return None
    head = ListNode(array[0])
    cur = head
    for value in array[1:]:
        cur.next = ListNode(value)
        cur = cur.next
    return head


def get_array_from_linked_list(head: ListNode) -> list[int]:
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


if __name__ == '__main__':
    c = None
    cases = [
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4]
        ),
        (
            ["LRUCache", "put", "get"],
            [[1], [2, 1], [2]],
            [None, None, 1]
        )
    ]
    for case in cases:
        res = []
        for op, args in zip(*case[:-1]):
            if op == "LRUCache":
                c = LRUCache(*args)
                res.append(None)
            elif op == "put":
                c.put(*args)
                res.append(None)
            elif op == "get":
                res.append(c.get(*args))
        print(res, case[-1])
