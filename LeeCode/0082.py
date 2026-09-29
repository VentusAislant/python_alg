class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """
        思路：
            因为链表是有序的
            使用一个 set 保存见过的数字，遇到重复的数字则一直往后知道下一个不重复的结点，然后将中间删除即可
            删除需要当前结点的 pre 结点，因此需要准备一个 pre 变量保存前一个结点
        """

        # 添加头结点方便统一处理
        dummy_head = ListNode(0, head)
        dummy_head.next = head

        seen = set()
        pre = dummy_head
        cur = head
        while cur:
            # 如果当前结点值重复
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                # 跳过所有重复值
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next

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
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
    ]
    solution = Solution()
    for case in cases:
        linked_lst = solution.construct_linked_list(case[0])
        # print(solution.get_linked_list(linked_lst))
        res = solution.get_linked_list(solution.deleteDuplicates(linked_lst))
        print(res, case[-1])
