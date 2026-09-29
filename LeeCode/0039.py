class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        V1版本中每次 backtrack 都需要计算 sum(path) 时间复杂度高，
        可以通过一个变量 remain 保存距离目标和还剩余多少来记录
        """
        res = []
        path = []
        n = len(candidates)

        def backtrack(start, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, n):
                path.append(candidates[i])
                backtrack(i, remain - candidates[i])
                path.pop()

        backtrack(0, target)
        return res

    def combinationSumV1(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        和计算组合数的关键区别是：
            原本的固定路径长度被替换为一个目标 target, 当 path 中的数字和 == target 时即可算作正确路径
            路径中的元素可以重复，即每次开始可以是上一次的开始
        """
        res = []
        path = []
        n = len(candidates)

        def backtrack(start):
            if sum(path) == target:
                res.append(path[:])
                return
            elif sum(path) > target:
                return

            for i in range(start, n):
                path.append(candidates[i])
                backtrack(i)
                path.pop()

        backtrack(0)
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [2, 3, 6, 7], 7,
            [[2, 2, 3], [7]]
        ),
        (
            [2, 3, 5], 8,
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        ),
        (
            [2], 1,
            []
        )
    ]
    for case in cases:
        res = solution.combinationSum(*case[:-1])
        print(res, case[-1])
