class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        """
        思路：
            需要找到倒数第 k + 1 个结点，记作 pre
            找到最后一个结点，记作 end
            将 pre 的后继设为 None, 将 pre.next 接到 dummy_head 后面，将 end 的后继设为 head 即可
        """
        if not head:
            return None

        # 有时候 k 大于链表长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        k = k % length
        if k == 0:
            return head

        dummy_head = ListNode(0, head)
        pre = dummy_head
        end = dummy_head  # end 比 pre 领先 k+1 个结点
        for _ in range(k):
            end = end.next

        while end.next is not None:
            pre = pre.next
            end = end.next

        end.next = head
        dummy_head.next = pre.next
        pre.next = None
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
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ]
    solution = Solution()
    for case in cases:
        linked_lst = solution.construct_linked_list(case[0])
        print(solution.get_linked_list(linked_lst))
        res = solution.get_linked_list(solution.rotateRight(linked_lst, case[1]))
        print(res, case[-1])
