class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        """
        不改变节点值，直接交换节点, 每次头插两个节点，注意不要丢失后面的节点信息

        情况1： p -> q -> r
            1. p -> r
            2. q -> p
            q -> p -> r
        情况2： a -> p -> q -> b
            1. p -> b
            2. a -> q
            3. q -> p
            a -> q -> p -> b

        可以直接使用一个占位头节点，统一上面的操作
        """
        if not head or not head.next:
            return head

        dummy_head = ListNode(0)
        dummy_head.next = head

        a = dummy_head

        while a.next and a.next.next:
            p = a.next
            q = a.next.next
            next_node = q.next

            p.next = next_node
            a.next = q
            q.next = p

            # 移动 a,准备下一轮
            a = p

        return dummy_head.next


def construct_linked_list(lst):
    head = ListNode(lst[0])
    cur = head
    for val in lst[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def linked_lst2lst(head: ListNode) -> list:
    if not head:
        return []

    cur = head
    lst = []
    while cur:
        lst.append(cur.val)
        cur = cur.next
    return lst


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
    ]
    solution = Solution()
    for case in cases:
        head = construct_linked_list(case[0])
        res = solution.swapPairs(head)
        print(linked_lst2lst(res), case[-1])
