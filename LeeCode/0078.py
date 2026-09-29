class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        回溯算法，对子集来说，核心规则如下：
            每个元素只能选一次
            不考虑顺序
        使用 path 记录当前子集, 每次都从 start 后面选一个元素, 执行流程
        设 nums = [1, 2, 3]
        backtrack(0), path = []
        ├── 记录 []                      → res = [[]]
        ├── 选择 nums[0] = 1
        │   backtrack(1), path = [1]
        │   ├── 记录 [1]                 → res = [[], [1]]
        │   ├── 选择 nums[1] = 2
        │   │   backtrack(2), path = [1,2]
        │   │   ├── 记录 [1,2]            → res = [[], [1], [1,2]]
        │   │   ├── 选择 nums[2] = 3
        │   │   │   backtrack(3), path = [1,2,3]
        │   │   │   └── 记录 [1,2,3]
        │   │   └── 回溯，path = [1,2]
        │   └── 回溯，path = [1]
        │   ├── 选择 nums[2] = 3
        │   │   backtrack(3), path = [1,3]
        │   │   └── 记录 [1,3]
        │   └── 回溯，path = [1]
        └── 回溯，path = []

        ├── 选择 nums[1] = 2
        │   backtrack(2), path = [2]
        │   ├── 记录 [2]
        │   ├── 选择 nums[2] = 3
        │   │   backtrack(3), path = [2,3]
        │   │   └── 记录 [2,3]
        │   └── 回溯，path = [2]
        └── 回溯，path = []

        ├── 选择 nums[2] = 3
        │   backtrack(3), path = [3]
        │   └── 记录 [3]
        └── 回溯，path = []

        """
        path = []
        res = []
        def backtrack(start: int):
            res.append(path.copy())

            for i in range(start, len(nums)):
                # 选择 nums[i]
                path.append(nums[i])
                backtrack(i + 1)
                # 撤销选择
                path.pop()

        backtrack(0)
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [1, 2, 3],
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        ),
        (
            [0],
            [[], [0]]
        )
    ]
    for case in cases:
        res = solution.subsets(*case[:-1])
        print(res, case[-1])
