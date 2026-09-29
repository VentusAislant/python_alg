class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """
        能否用 O(1) 的空间？
        可以看成走路问题，一个人从 A 出发 一个人从 B 出发，每次都走一步
        假设 A 和 B 交叉长度为 c, A和B独自的不交叉的长度分别为 a,b
        如果两个人都走 a+b+c 步骤，如果走到尽头，则从另一条路的开始继续走
            A 和 B 最终走到交叉点位置
        时间复杂度 O(M+N)
        空间复杂度 O(1)
        """
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA

        return p


    def getIntersectionNodeV2(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """
        可以先遍历一个链表，将其存入哈希表中，然后遍历另一个链表，判断每个结点是否已经出现在哈希表中，
        如果出现则是交叉点
        时间复杂度 O(M+N)
        空间复杂度 O(M)
        """
        hash_map = set()
        cur = headA
        while cur:
            hash_map.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in hash_map:
                return cur
            cur = cur.next
        return None

    def getIntersectionNodeV1(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """
        交叉点之后的结点必然都是相同的，可以利用这个特点从后往前找到第一个不同的元素，上一个相同的元素几位所求
        时间复杂度 O(M+N)
        空间复杂度 O(M+N)
        """
        stack1, stack2 = [], []
        cur1, cur2 = headA, headB
        while cur1:
            stack1.append(cur1)
            cur1 = cur1.next
        while cur2:
            stack2.append(cur2)
            cur2 = cur2.next

        if stack1[-1] != stack2[-1]:
            return None
        else:
            while stack1 and stack2 and stack1[-1] == stack2[-1]:
                res = stack1.pop()
                stack2.pop()
            return res



def construct_cross_linked_list(
        intersect_val,  # 相交的起始节点的值。如果不存在相交节点，这一值为 0
        list1: list,  # 第一个链表元素
        list2: list,  # 第二个链表元素
        skip1: int,  # 在 list1 中（从头节点开始）跳到交叉节点的节点数
        skip2: int  # 在 list2 中（从头节点开始）跳到交叉节点的节点数
) -> list[ListNode | None]:
    head1, head2 = ListNode(0), ListNode(0)  # dummy head
    cur1, cur2 = head1, head2
    i, j = 0, 0
    while i < skip1:
        cur1.next = ListNode(list1[i])
        cur1 = cur1.next
        i += 1

    while j < skip2:
        cur2.next = ListNode(list2[j])
        cur2 = cur2.next
        j += 1

    while i < len(list1) or j < len(list2):
        node = ListNode(list1[i])
        cur1.next = node
        cur2.next = node
        cur1 = cur1.next
        cur2 = cur2.next
        i += 1
        j += 1

    return [head1.next, head2.next]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3,
            "Intersected at '8'"
        ),
        (
            2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1,
            "Intersected at '2'"
        ),
        (
            0, [2, 6, 4], [1, 5], 3, 2,
            "No intersection"
        )
    ]
    for case in cases:
        head1, head2 = construct_cross_linked_list(
            *case[:-1]
        )
        res = solution.getIntersectionNode(head1, head2)
        res = 'No intersection' if res is None else f"Intersected at '{res.val}'"
        print(res, case[-1])
