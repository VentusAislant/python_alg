class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        删除倒数第 N 个结点，关键是找到倒数第 N+1 个结点
        可以通过两个相差 N 步的指针来只扫描一遍找到这两个结点
        假设第一个结点为 p, p 往后 N 个结点为 q，当 q 到达最后 None 结点时， p 指向倒数第 N 个结点
        """

        # 方便统一处理需要删除头结点的情况
        dummy = ListNode(0)
        dummy.next = head

        p = dummy  # 记录倒数第 N+1 个结点
        q = dummy  # 用于辅助找到倒数第 N+1 个结点
        for _ in range(n + 1):
            q = q.next

        while q:
            p = p.next
            q = q.next

        # 此时 p 指向倒数 第 N+1 个结点
        p.next = p.next.next
        return dummy.next

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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ]
    solution = Solution()
    for case in cases:
        linked_lst = solution.construct_linked_list(case[0])
        print(solution.get_linked_list(linked_lst))
        res = solution.get_linked_list(solution.removeNthFromEnd(linked_lst, case[1]))
        print(res, case[-1])
