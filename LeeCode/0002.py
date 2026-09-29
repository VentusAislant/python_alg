class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """
        由于两个 list 保存的是逆序的数字字符，因此可以直接模拟加法操作，利用一个变量 carry 保存进位信息，从左往右相加即可
        有两个注意的地方：
            1. 如果 l1 和 l2 不等长，怎么处理剩下的元素，需要防止断链
            2. 如果最后进位变量存的值不等于0 需要添加额外的节点

        """
        carry = 0
        node1 = l1
        node2 = l2
        pre_node = None  # 在 l1 和 l2 不等长情况下，需要记录一下最后一个结点，防止断链

        while node1 and node2:
            if node1.val + node2.val + carry > 9:
                tmp = node1.val + node2.val + carry
                node1.val = tmp % 10
                carry = tmp // 10
            else:
                node1.val += node2.val + carry
                carry = 0

            pre_node = node1  # 使用 l1 来保存最后结果
            node1 = node1.next
            node2 = node2.next

        # 如果 l1 比 l2 长，将 l1 剩余元素加上 carry 拼接到链表尾
        while node1:
            if node1.val + carry > 9:
                tmp = node1.val + carry
                node1.val = tmp % 10
                carry = tmp // 10
            else:
                node1.val += carry
                carry = 0
            pre_node = node1
            node1 = node1.next

        # 如果 l2 比 l1 长，则 node1 所指为 None, 断链，可以采用 pre_node 来进行操作
        while node2:
            if node2.val + carry > 9:
                tmp = node2.val + carry
                node2.val = tmp % 10
                carry = tmp // 10
            else:
                node2.val += carry
                carry = 0

            pre_node.next = node2
            pre_node = pre_node.next
            node2 = node2.next

        # 最后还有额外的进位信息则需要添加结点
        while carry > 0:
            pre_node.next = ListNode(carry % 10)
            carry = carry // 10
            pre_node = pre_node.next

        return l1

    def addTwoNumbersV1(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """
        简单做法：先转成 int, 然后计算结果再转化为链表
        时间复杂度: O(M+N)
        空间复杂度： O(M+N)
        """
        elements1 = []
        elements2 = []
        node1 = l1
        while node1:
            elements1.append(node1.val)
            node1 = node1.next

        node2 = l2
        while node2:
            elements2.append(node2.val)
            node2 = node2.next

        elements1.reverse()
        elements2.reverse()

        num1, num2 = 0, 0
        for element in elements1:
            num1 = num1 * 10 + element

        for element in elements2:
            num2 = num2 * 10 + element

        num3 = num1 + num2
        if num3 == 0:
            return construct_linked_list([0])

        elements3 = []
        while num3 > 0:
            elements3.append(num3 % 10)
            num3 = num3 // 10
        return construct_linked_list(elements3)


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
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([2, 4], [5, 6, 4], [7, 0, 5]),
        ([2, 4, 3], [5, 6], [7, 0, 4]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
    ]
    solution = Solution()
    for case in cases:
        print('=' * 90)
        l1 = construct_linked_list(case[0])
        l2 = construct_linked_list(case[1])
        print(linked_list2list(l1), linked_list2list(l2))
        l3 = solution.addTwoNumbersV1(l1, l2)
        print(linked_list2list(l3), case[-1])
