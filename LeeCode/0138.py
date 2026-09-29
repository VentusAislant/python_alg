class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        """
        改进，如何使用 O(1)的空间复杂度？
            关键是需要有原结点和克隆结点的映射关系，才能构建 random 链条
            可以利用原链，将克隆结点插入到原链对应结点的后面，构建完 random 链后，重新拆分链表构建 next 链
        时间复杂度 O(N)
        空间复杂度 O(1)
        """
        if not head:
            return None

        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            # 此时下一个结点是 cur.next.next
            cur = cur.next.next

        # 构建 random 链
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random is not None else None
            cur = cur.next.next

        # 拆分
        cur = head
        clone_head = head.next
        while cur:
            clone = cur.next
            cur.next = clone.next
            if clone.next:
                clone.next = clone.next.next
            cur = cur.next
        return clone_head

    def copyRandomListV1(self, head: Node | None) -> Node | None:
        """
        简单思路： 遍历两次
        第一次克隆所有结点，但不连指针，建立原始结点到克隆结点的映射表
        第二次构建 next 和 random 指针链条，利用哈希表中的结点即可
        时间复杂度 O(N)
        空间复杂度 O(N)
        """
        if head is None:
            return None

        org2clone = {}
        cur = head
        while cur:
            org2clone[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                org2clone[cur].next = org2clone[cur.next]
            if cur.random:
                org2clone[cur].random = org2clone[cur.random]
            cur = cur.next

        return org2clone[head]


def construct_linked_list(lst):
    """
    两遍遍历，第一遍构建结点和 next 链，第二遍构建 random 链
    """
    if not lst:
        return None

    idx2Node = {0: Node(lst[0][0])}
    cur = idx2Node[0]

    # 构建映射表，并构建 next 链
    for i in range(1, len(lst)):
        cur.next = Node(lst[i][0])
        idx2Node[i] = cur.next
        cur = cur.next

    # 构建 random 链
    for idx, (_, random_idx) in enumerate(lst):
        if random_idx is None:
            idx2Node[idx].random = None
        else:
            idx2Node[idx].random = idx2Node[random_idx]

    return idx2Node[0]


def get_linked_lst(head: None) -> list:
    if head is None:
        return []

    # 第一遍：构建 Node 到索引的映射
    Node2idx = {}
    cur = head
    idx = 0
    while cur:
        Node2idx[cur] = idx
        cur = cur.next
        idx += 1

    # 第二遍：写入每个结点的 (val, random_index)
    res = []
    cur = head
    while cur:
        random_idx = Node2idx[cur.random] if cur.random else None
        res.append((cur.val, random_idx))
        cur = cur.next

    return res


if __name__ == '__main__':
    cases = [
        (
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        ),
        (
            [[1, 1], [2, 1]],
            [[1, 1], [2, 1]]
        ),
        (
            [[3, None], [3, 0], [3, None]],
            [[3, None], [3, 0], [3, None]]
        ),
    ]
    solution = Solution()
    for case in cases:
        l1 = construct_linked_list(case[0])
        # print(get_linked_lst(l1))
        res = solution.copyRandomList(l1)
        print(get_linked_lst(res), case[-1])
