class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        """
        改进：回想链表的头插法，可以反转链表，可以参考头插法思路，找到 left 前一个结点 prev
            记 left 位置处的结点为 cur, 不断将 cur 后面的结点插入到 prev 后面，最后即可完成逆置
        """
        dummy_head = ListNode(0, head)

        # 1. 找到 pre 结点
        prev = dummy_head
        for _ in range(left - 1):
            prev = prev.next

        # 不断头插 cur 后面的结点，注意不能断链
        cur = prev.next
        for _ in range(right - left):
            next_node = cur.next  # 将 cur 后面的结点插入到 prev 后
            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy_head.next

    def reverseBetweenV1(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        """
        转化成数组，反转后，再转化成链表
        """
        lst = self.get_linked_list(head)
        i, j = left - 1, right - 1
        while i < j:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
            j -= 1
        return self.construct_linked_list(lst)

    def construct_linked_list(self, lst: list[int]) -> ListNode | None:
        if len(lst) == 0: return None
        head = ListNode(lst[0])
        cur_node = head
        for val in lst[1:]:
            cur_node.next = ListNode(val)
            cur_node = cur_node.next
        return head

    def get_linked_list(self, head):
        cur_node = head
        res = []
        while cur_node:
            res.append(cur_node.val)
            cur_node = cur_node.next
        return res


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
    ]
    solution = Solution()
    for case in cases:
        linked_lst = solution.construct_linked_list(case[0])
        # print(solution.get_linked_list(linked_lst))
        res = solution.get_linked_list(solution.reverseBetween(linked_lst, case[1], case[2]))
        print(res, case[-1])
