class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge2Lists(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        p, q = head1, head2
        while p and q:
            if p.val < q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next

            cur = cur.next
        cur.next = p if p is not None else q
        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        两个升序链表归并较为容易，可以将 K 个链表的归并，递归到两个两个链表的归并
        """
        if not lists: return None

        def merge(start, size):
            """
            合并 lists[start:start+size] 的部分
            """
            if size == 0: return None
            if size == 1:
                return lists[start]

            half = size // 2
            left_head = merge(start, half)
            right_head = merge(start + half, size - half)
            return self.merge2Lists(left_head, right_head)

        return merge(0, len(lists))


def lst2linked_lst(lst: list[int]) -> ListNode | None:
    if len(lst) == 0: return None
    head = ListNode(lst[0])
    cur_node = head
    for val in lst[1:]:
        cur_node.next = ListNode(val)
        cur_node = cur_node.next
    return head


def linked_lst2lst(head) -> list:
    cur_node = head
    res = []
    while cur_node:
        res.append(cur_node.val)
        cur_node = cur_node.next
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [[1, 4, 5], [1, 3, 4], [2, 6]],
            [1, 1, 2, 3, 4, 4, 5, 6]
        ),
        (
            [],
            []
        ),
        (
            [[]],
            []
        )
    ]
    for case in cases:
        input = [lst2linked_lst(lst) for lst in case[0]]
        linked_lst = solution.mergeKLists(input)
        res = linked_lst2lst(linked_lst)
        print(res, case[-1])
