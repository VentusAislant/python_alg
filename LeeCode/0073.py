class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        使用第一行和第一列作为记录空间，第一遍遍历将需要归0的列记录到第一行，需要归0的行记录到第一列
        第一行和第一列需要特殊处理，用两个标志在覆盖之前记录是否需要归0
        """
        m, n = len(matrix), len(matrix[0])
        row0 = any(matrix[0][j] == 0 for j in range(n))  # 第一行是否需要置零
        col0 = any(matrix[i][0] == 0 for i in range(m))  # 第一列是否需要置零

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 第一行和第一列已经更新过了，更新除了第一行第一列的元素
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if col0:
            for i in range(m):
                matrix[i][0] = 0
        if row0:
            for j in range(n):
                matrix[0][j] = 0

    def setZeroesV1(self, matrix: list[list[int]]) -> None:
        """
        先记录所有需要删除的行和列，然后进行删除
        使用了额外的空间，不满足题目要求
        空间复杂度 O(M+N)
        """
        to_delete_i = set()
        to_delete_j = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    to_delete_i.add(i)
                    to_delete_j.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in to_delete_i or j in to_delete_j:
                    matrix[i][j] = 0


if __name__ == '__main__':
    cases = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
    ]
    solution = Solution()
    for case in cases:
        solution.setZeroes(case[0])
        print(case[0], case[1])
