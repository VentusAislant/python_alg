class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        关键信息，每个数字都在 [1,n], 数组长度为 n+1， 不修改数组，只能用 O(1) 空间
            所以所有数组元素可以看作一个合法的索引
            [1, 3, 4, 2, 2]
            nums[0] -> 1
            nums[1] -> 3
            nums[3] -> 2
            nums[2] -> 4
            nums[4] -> 2
            nums[2] -> 4
            ... 出现了环
            head -> 1 -> 3 -> 2 -> 4 -> 2循环
        转换成找环的入口问题，就可以用快慢指针法了 参见 142 环形链表II
        """
        slow = nums[0]
        fast = nums[0]

        # 找到相遇点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 找到环的入口
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast


if __name__ == '__main__':
    cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3)
    ]
    solution = Solution()
    for case in cases:
        res = solution.findDuplicate(case[0])
        print(res, case[-1])
