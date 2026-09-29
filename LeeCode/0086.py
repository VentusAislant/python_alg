class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        """
        思路：
            使用两个头结点 dummy_smaller, dummy_greater， 后面分别接入小于或大于 x 的结点
            最后将 dummy_smaller_end.next = dummy_greater.next
        """
        dummy_smaller = ListNode(0)
        dummy_greater = ListNode(0)

        cur = head
        cur_smaller = dummy_smaller
        cur_greater = dummy_greater
        while cur:
            if cur.val < x:

                cur_smaller.next = cur
                cur_smaller = cur_smaller.next
            else:
                cur_greater.next = cur
                cur_greater = cur_greater.next
            cur = cur.next

        # 断开 greater 链表，否则会形成环
        cur_greater.next = None
        cur_smaller.next = dummy_greater.next
        return dummy_smaller.next


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
    solution = Solution()
    cases = [
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2])
    ]
    for case in cases:
        linked_list = construct_linked_list(case[0])
        res_link_list = solution.partition(linked_list, case[1])
        res_array = get_array_from_linked_list(res_link_list)
        print(res_array, case[-1])
