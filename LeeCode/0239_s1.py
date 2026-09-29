from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        简单解法：滑动窗口过程中求每个窗口最大值
        如何改进，每次都求最大值使得复杂度变为 O(n^2)
        使用单调递减队列，维护一个双端队列 queue
            存的是下标，并且队列中的元素对应的值从队首到队尾严格递减

        这个问题的核心思想是：在滑动窗口移动的过程中，并不是每个元素都有资格成为窗口中的最大值。
        我们只需要维护一组“可能成为最大值”的候选元素，并保证它们按从大到小的顺序排列。
        当一个新元素进入窗口时，所有在它左边且比它小的元素都可以直接丢弃，因为只要新元素还在窗口内，
        它们永远不可能成为最大值；当窗口向右滑动时，如果当前最大值已经滑出窗口，也需要将它移除。
        这样一来，窗口中的最大值始终可以在常数时间内得到，整体只需线性时间完成。

        [3, 3, 5, 5, 6, 7]  k=3
        i=?   queue=?  res=?
        0     [0]      []
        1     [0, 1]   []
        2     [2]      [5]
        3     [2,3]    [5, 5]
        4     [6]      [5, 5, 6]
        5     [7]      [5, 5, 6, 7]

        [1, 3, -1, -3, 5, 3, 6, 7]  k=3
        i=?         queue=?         res=?
        0           [0]             []
        1           [1]             []
        2           [1,2]           [3]
        3           [1,2,3]         [3, 3]
        4           [4]             [3, 3, 5]
        5           [4,5]           [3, 3, 5, 5]
        6           [6]             [3, 3, 5, 5, 6]
        7           [7]             [3, 3, 5, 5, 6, 7]
        """
        if len(nums) < k:
            return [max(nums)]

        res = []
        queue = deque([])
        for i in range(len(nums)):
            # 把右边比当前数小的剔除，维护队列的单调性
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            # 当前元素可以插入队尾
            queue.append(i)

            # 如果队首已经在窗口之外，则剔除
            if queue[0] <= i - k:
                queue.popleft()

            # 在第一个窗口形成后开始取窗口最大值，即队首元素
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res

    def maxSlidingWindowV1(self, nums: list[int], k: int) -> list[int]:
        """
        简单解法：滑动窗口过程中求每个窗口最大值
        会超时
        """
        if len(nums) < k:
            return [max(nums)]

        result = []
        left, right = 0, k - 1
        while right < len(nums):
            result.append(max(nums[left:right + 1]))
            left += 1
            right += 1

        return result


if __name__ == '__main__':
    cases = [
        (
            [1, 3, -1, -3, 5, 3, 6, 7], 3,
            [3, 3, 5, 5, 6, 7]
        ),
        (
            [1], 1,
            [1]
        ),
        (
            [3, 3, 5, 5, 6, 7], 3,
            [5, 5, 6, 7]
        )
    ]

    solution = Solution()
    for case in cases:
        res = solution.maxSlidingWindow(*case[:-1])
        print(res, case[-1])
