class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """
        迭代法，要把  1 -> 2 -> 3 -> None 变为 None <- 1 <- 2 <- 3 即可
        """
        pre = None
        cur = head
        while cur:
            next_node = cur.next  # 保存原来的后继信息避免丢失
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


    def reverseListV2(self, head: ListNode | None) -> ListNode | None:
        """
        递归法，要把  1 -> 2 -> 3 -> None
        先反转后面的链表，再把当前节点接到最后即
        reverse(i) 返回已经反转第 i 个节点后的子链表头
        """
        def reverse(node: ListNode| None) -> ListNode:
            if node is None or node.next is None:
                return node

            # 递归反转后面的链表
            new_head = reverse(node.next)

            # 将当前节点拼到反转好的后面的链表后
            node.next.next = node

            # 当前节点在末尾，所以断开之前的链
            node.next = None
            return new_head
        return reverse(head)

    def reverseListV1(self, head: ListNode | None) -> ListNode | None:
        """
        头插法，只需要遍历一遍
        """
        dummy_head = ListNode(0)
        cur = head
        while cur:
            next_node = cur.next
            cur.next = dummy_head.next
            dummy_head.next = cur
            cur = next_node
        return dummy_head.next


def construct_linked_list(elements: list) -> ListNode | None:
    if not elements:
        return None

    linked_list = ListNode(elements[0])
    cur_node = linked_list
    for i in range(1, len(elements)):
        new_node = ListNode(elements[i])
        cur_node.next = new_node
        cur_node = new_node
    return linked_list


def linked_list2list(linked_list: ListNode) -> list:
    cur_node = linked_list
    res_lst = []
    while cur_node:
        res_lst.append(cur_node.val)
        cur_node = cur_node.next
    return res_lst


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([], [])
    ]
    solution = Solution()
    for case in cases:
        print('=' * 90)
        l1 = construct_linked_list(*case[:-1])
        l2 = solution.reverseListV2(l1)
        print(linked_list2list(l2), case[-1])
