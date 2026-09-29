class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        可以采用快慢指针，慢指针每次走1步，快指针每次走2步
            如果存在环，则慢指针会和快指针相遇
            如果不存在环，则快指针会先到达链表尾
        时间复杂度 O(N)
        空间复杂度 O(1)
        """
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def hasCycleV1(self, head: ListNode) -> bool:
        """
        可以利用一个哈希表存储已经遍历过的结点，如果遍历过程中遇到过遍历过的结点则存在环
        时间复杂度 O(N)
        空间复杂度 O(N)
        """
        seen = set()
        cur_node = head
        while cur_node:
            if cur_node in seen:
                return True
            seen.add(cur_node)
            cur_node = cur_node.next
        return False


def construct_cycled_linked_list(elements: list, pos: int = -1) -> ListNode | None:
    if not elements:
        return None

    cycled_node = None
    linked_list = ListNode(elements[0])
    cur_node = linked_list
    if pos == 0:
        cycled_node = cur_node
    for i in range(1, len(elements)):
        new_node = ListNode(elements[i])
        if pos == i:
            cycled_node = cur_node
        cur_node.next = new_node
        cur_node = new_node

    cur_node.next = cycled_node
    return linked_list


if __name__ == '__main__':
    cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
    ]
    solution = Solution()
    for case in cases:
        head = construct_cycled_linked_list(case[0], case[1])
        res = solution.hasCycle(head)
        print(res, case[-1])
