class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def right_move_k(self, node: ListNode, k: int) -> ListNode | None:
        cur = node
        for _ in range(k):
            if cur:
                cur = cur.next
            else:
                return None
        return cur

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """
        使用两个指针记录每一段的开头的前一个结点和结尾结点，
        对每一段使用头插法进行翻转
        """
        if k == 1 or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        while self.right_move_k(cur, k) is not None:
            next_node = cur.next

            # 翻转这一段
            # cur 表示头插法的虚拟头结点
            to_append = cur.next
            cur.next = None
            for _ in range(k):
                next_to_append = to_append.next
                to_append.next = cur.next
                cur.next = to_append
                to_append = next_to_append

            next_node.next = to_append
            cur = next_node

        return dummy.next

    def reverseKGroupV1(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 1:
            return head

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        num_groups = length // k
        left = 1
        right = k
        for _ in range(num_groups):
            head = self.reverseBetween(head, left, right)
            left += k
            right += k
        return head

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
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ]
    solution = Solution()
    for case in cases:
        linked_lst = solution.construct_linked_list(case[0])
        # print(solution.get_linked_list(linked_lst))
        res = solution.get_linked_list(solution.reverseKGroup(linked_lst, case[1]))
        print(res, case[-1])
