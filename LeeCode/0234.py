class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        """
        V2版本的另一种写法，反转后半部分链表，而不是前半部分，代码更简洁
        """
        if not head or not head.next:
            return True

        # 1. 快慢指针找到重点
        slow, fast = head, head
        slow_prev = None
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        # 2. 处理奇数情况，如果是奇数则 fast 不是 None, 否则是 None
        if fast is not None:
            slow_prev = slow
            slow = slow.next  # 指向后半部分链表的第一个结点

        # 3. 反转后半段链表
        dummy_head = ListNode(0)
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = dummy_head.next
            dummy_head.next = cur
            cur = next_node

        # 4. 判断是否是回文
        res = True
        p1, p2 = head, dummy_head.next
        while p2:
            if p1.val != p2.val:
                res = False
            p1 = p1.next
            p2 = p2.next

        # 5. 恢复链表
        cur = dummy_head.next
        dummy_head.next = None
        while cur:
            next_node = cur.next
            cur.next = dummy_head.next
            dummy_head.next = cur
            cur = next_node
        slow_prev.next = dummy_head.next
        return res


    def isPalindromeV2(self, head: ListNode | None) -> bool:
        """
        能否用 O(1) 空间复杂度，即不用栈如何记录前半部分元素的逆置链表
            用一个 dummy_head 头插法插入前半部分结点，然后判断
        """
        if not head or not head.next:
            return True

        # 1. 快慢指针找到重点
        dummy_head = ListNode(0)
        p, q = head, head.next  # p每次走1步，q每次走两步
        while q and q.next:
            next_node = p.next
            # 头插法插入
            p.next = dummy_head.next
            dummy_head.next = p

            p = next_node
            q = q.next.next

        next_node = p.next
        p.next = dummy_head.next
        dummy_head.next = p

        res = True
        # q 为 None 表示奇数个
        h1 = dummy_head.next.next if q is None else dummy_head.next
        h2 = next_node

        while h1 and h2:
            if h1.val != h2.val:
                res = False
                break
            h1 = h1.next
            h2 = h2.next

        # 恢复链表
        cur = dummy_head.next
        dummy_head.next = next_node
        while cur:
            nex_node = cur.next
            cur.next = dummy_head.next
            dummy_head.next = cur
            cur = nex_node
        return res

    def isPalindromeV1(self, head: ListNode | None) -> bool:
        """
        最简单的思路，利用一个栈存前半段元素，然后遍历后半段元素，同时弹出栈
        空间复杂度 O(N/2)
        时间复杂度 O(N)
        """
        if not head:
            return False
        if head.next is None:
            return True

        stack = []
        p, q = head, head.next  # p每次走1步，q每次走两步
        while q and q.next:
            stack.append(p)
            p = p.next
            q = q.next.next
        stack.append(p)

        if q is None:  # 奇数个元素
            stack.pop()

        cur = p.next  # 后半段链表的第一个结点
        while cur:
            if cur.val != stack[-1].val:
                return False
            cur = cur.next
            stack.pop()
        return True


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
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1, 0, 0], False),
    ]
    solution = Solution()
    for case in cases:
        head = construct_linked_list(*case[:-1])
        print(linked_list2list(head))
        res = solution.isPalindrome(head)
        print(res, case[-1])
