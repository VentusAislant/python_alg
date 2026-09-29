class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        回溯算法，使用一个 path 表示当前选择的结点，path会增加也会减少
        使用一个 used 列表记录当前某个结点是否已经使用过
        """
        res = []
        path = []  # 表示当前已经选择的结点
        used = [False] * len(nums)  # 用来记录某个结点是否已经使用过，防止重复使用元素

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            """
            假设 nums = [1, 2, 3]
            对于 i = 0 会执行如下步骤
                path = [1]          used = [True, False, False]
                path = [1, 2]       used = [True, True, False]
                path = [1, 2, 3]    used = [True, True, True]
                path = [1, 3]       used = [True, False, True]
                path = [1, 3, 2]    used = [True, True, True]
            """
            for i in range(len(nums)):
                if used[i]:  # 跳过已经选择过的
                    continue

                # 选择当前结点
                path.append(nums[i])
                used[i] = True
                backtrack()

                # 撤销选择
                path.pop()
                used[i] = False

        backtrack()
        return res

    def permuteV1(self, nums: list[int]) -> list[list[int]]:
        """
        递归的方式，假设当前有四个数 [1, 2, 3, 4]
            可以知道当前的全排列等于
                1 + [2, 3, 4]的全排列
                2 + [1, 3, 4]的全排列
                3 + [1, 2, 4]的全排列
                4 + [1，2, 3]的全排列
            可以递归的进行
        """

        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            cur_nums = [] + nums[:i] + nums[i + 1:]
            cur_permutes = self.permuteV1(cur_nums)
            for j in range(len(cur_permutes)):
                cur_permutes[j] = [nums[i]] + cur_permutes[j]
            res += cur_permutes
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        ),
        (
            [0, 1],
            [[0, 1], [1, 0]]
        )
    ]
    for case in cases:
        res = solution.permute(*case[:-1])
        print(res, case[-1])
