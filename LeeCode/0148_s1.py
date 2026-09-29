class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find_mid(self, head: ListNode) -> ListNode:
        """
        可以采用快慢指针，慢指针每次走1步，快指针每次走2步，快指针到达
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 if l1 else l2
        return dummy.next

    def sortList(self, head: ListNode | None) -> ListNode | None:
        """
        要求时间复杂度 O(N*logN) 空间复杂度 O(1)
        可以参考归并排序思想，分别对左右链表递归进行排序即可，然后对两个排序的链表进行归并
        """
        if not head:
            return None

        if head.next is None:
            return head  # 只有一个元素，已经有序

        mid_node = self.find_mid(head)  # O(N)
        right_head = mid_node.next
        mid_node.next = None

        # O(logN)
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_head)
        return self.merge(left_sorted, right_sorted)  # O(N)


def lst2_linked_list(nums: list) -> ListNode | None:
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


def linked_lst2lst(head: ListNode) -> list:
    if not head:
        return []
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [4, 2, 1, 3],
            [1, 2, 3, 4]
        ),
        (
            [-1, 5, 3, 4, 0],
            [-1, 0, 3, 4, 5]
        )
    ]
    for case in cases:
        head = lst2_linked_list(*case[:-1])
        head = solution.sortList(head)
        res = linked_lst2lst(head)
        print(res, case[-1])
