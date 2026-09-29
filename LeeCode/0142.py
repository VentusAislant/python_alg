class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        """
        快慢指针： slow 每次走一步， fast 每次走两步
            假设链表长度为 n, 非环部分长度为 a, slow 指针进入 环后走了 b, 环中的另一部分长度为 c
            此时 fast 指针已经走完了环的 m 圈， 总距离为 a + m(b+c) + b = a + (m+1)b + mc

            由于任意时刻 fast 走过的距离都是 slow 的两倍，因此有
                a + (m+1)b + mc = 2(a+b)
                -a + (m-1)b + mc = 0
                a = (m-1)(b+c) + c

            可以发现，从相遇点到入环点的距离 c 加上 n-1 圈的环长，正好等于链表头到入环点的距离
            因此在 slow 和 fast 相遇后，再用一个额外指针 ptr 从头开始，
            ptr 和 slow 每次都走一步，必定会在入环点相遇
        """
        if not head or not head.next:
            return None

        # 判断是否有环
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        if slow != fast:
            return None

        # 找环的入口
        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return fast

    def detectCycleV1(self, head: ListNode | None) -> ListNode | None:
        """
        最简单的思路，使用一个哈希表存储遍历过的结点，第二次首先出现的结点环的开始
        空间复杂度 O(N) 时间复杂度 O(N)
        """
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next

        return None


def construct_cycle_linked_list(elements: list, cycle_start=-1) -> ListNode | None:
    if not elements:
        return None

    head = ListNode(elements[0])
    cycle_node = head if cycle_start == 0 else None
    cur_node = head
    for i in range(1, len(elements)):
        new_node = ListNode(elements[i])
        cur_node.next = new_node
        cur_node = new_node
        if i == cycle_start:
            cycle_node = cur_node
    cur_node.next = cycle_node
    return head


if __name__ == '__main__':
    cases = [
        ([3, 2, 0, -4], 1, 2),
        ([1, 2], 0, 1),
        ([1], -1, None),
    ]
    solution = Solution()
    for case in cases:
        print('=' * 90)
        head = construct_cycle_linked_list(*case[:-1])
        res = solution.detectCycle(head)
        print(res if not res else res.val, case[-1])
