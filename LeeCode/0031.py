class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        首先观察一下字典序
            [1, 2, 3] < [1, 3, 2] < [2, 1, 3] < [2, 3, 1] < [3, 1, 2] < [3, 2, 1]

            如何比较两个排列的字典序大小？
                从左往右找到第一个不同的数字，然后比较其大小即可
            一些观察：
                升序序列是最小的排列，降序序列是最大的排列
            如何让一个排列字典序变大的较小？
                1. 首先从右往左找到下降点，
                    如 [1, 2, 3] 中的 2， [1, 3, 2]中的 1， [2, 2, 7, 5, 4, 3, 2, 2, 1] 中的 第二个 2
                    这个点可以保证尽可能减少对高位的干扰，让上升幅度尽可能小，同时保证后面有大于其的数有上升空间
                2. 其次从这个点右侧的降序序列中找到比这个下降点的值高的最小的元素，来使得上升幅度尽可能小
                    如 [1, 2, 3] 中的 3, [1, 3, 2] 中的 2, [2, 2, 7, 5, 4, 3, 2, 2, 1] 中的 3
                3. 交换这个两个位置
                    [1, 2, 3] -> [1, 3, 2]  [1, 3, 2] -> [2, 3, 1]
                    [2, 2, 7, 5, 4, 3, 2, 2, 1] -> [2, 3, 7, 5, 4, 2, 2, 1]
                4. 保证下降点右边的序列还是递增序列，来使其尽可能小，原来是递增现在反转即可
                    [1, 3, 2] -> [1, 3, 2]  [2, 3, 1] -> [2, 1, 3]
                    [2, 3, 7, 5, 4, 2, 2, 1] -> [2, 3, 1, 2, 2, 4, 5, 7]
        """
        n = len(nums)
        # 从右往左找第一个下降点
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 找到右侧比下降点大的最少的数, 右侧的数字从有往左是一个升序序列
        if i >= 0:
            j = n - 1
            while j > 0 and nums[j] <= nums[i]:
                j -= 1

            # 交换这两个数
            nums[i], nums[j] = nums[j], nums[i]

        # 反转下降点右侧的数
        nums[i + 1:] = reversed(nums[i + 1:])

    def permutation(self, nums: list[int]) -> list[list[int]]:
        """
        返回 nums 的全排列
        """
        path = []
        used = [False] * len(nums)
        res = []

        def backtrack():
            if len(path) == len(nums) and path not in res:
                res.append(path[:])  # 必须是复制版本，不能是引用

            for i in range(len(nums)):
                # 选择 nums[i]
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res

    def nextPermutationV1(self, nums: list[int]) -> None:
        """
        暴力解法，直接写出所有字典序排列，然后找到当前排列的下一个
        时间复杂度 O(n*n!):
            生成全排列 O(n*n!) 复制路径用到 n， 共有 n! 个排列
            排序复杂度 O(nlogn) 可以忽略
            查找排列位置 O(n*n!) O(n) 用来比较两个数组，共有 n! 个数组
            赋值 nums O(n)
        空间复杂度 O(n*n!)
            保存排列 O(n*n!)
            回溯最深 O(n)
        """
        permutation_lst = self.permutation(sorted(nums))
        pos = -1
        for i in range(len(permutation_lst)):
            if all(a == b for a, b in zip(permutation_lst[i], nums)):
                pos = i
                break
        nums[:] = permutation_lst[(pos + 1) % len(permutation_lst)]  # 不能仅仅修改 nums 引用


if __name__ == '__main__':
    cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 5, 1], [5, 1, 1]),
        ([2, 2, 7, 5, 4, 3, 2, 2, 1], [2, 3, 1, 2, 2, 2, 4, 5, 7])
    ]
    solution = Solution()
    for case in cases:
        solution.nextPermutation(case[0])
        res = case[0]
        print(res, case[-1])
