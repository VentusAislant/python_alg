class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """
        标准的归并实现
        """
        p, q = list1, list2
        dummy = ListNode(0)  # 一个空的头结点
        cur = dummy
        while p and q:
            if p.val < q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next

            cur = cur.next

        # 剩余的部分直接挂到链表尾部
        cur.next = p if p else q
        return dummy.next


def construct_linked_list(lst: list[int]) -> ListNode | None:
    if len(lst) == 0: return None
    head = ListNode(lst[0])
    cur_node = head
    for val in lst[1:]:
        cur_node.next = ListNode(val)
        cur_node = cur_node.next
    return head


def get_linked_list(head):
    cur_node = head
    res = []
    while cur_node:
        res.append(cur_node.val)
        cur_node = cur_node.next
    return res


if __name__ == '__main__':
    cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]
    solution = Solution()
    for case in cases:
        list1 = construct_linked_list(case[0])
        list2 = construct_linked_list(case[1])
        # print(get_linked_list(list1), get_linked_list(list2))
        res = get_linked_list(solution.mergeTwoLists(list1, list2))
        print(res, case[-1])
