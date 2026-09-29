class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        关键点：矩阵越往右下数越大，利用这个性质每次比较排除一行一列
            右上角元素，是该行最大，该列最小的，所以通过比较可以排除一行或一列
        时间复杂度 O(M+N)
        空间复杂度 O(1)
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                # 应该在左侧，排除这一列比 matrix[i][j] 更大的
                j -= 1
            else:
                # 应该在下恻，排除这一行比 matrix[i][j] 更小的
                i += 1
        return False

if __name__ == '__main__':
    cases = [
        (
            [[1, 4, 7, 11, 15],
             [2, 5, 8, 12, 19],
             [3, 6, 9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 21, 23, 26, 30]],
            20,
            False,
        ),

        (
            [[1, 4, 7, 11, 15],
             [2, 5, 8, 12, 19],
             [3, 6, 9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 21, 23, 26, 30]],
            5,
            True,
        ),
        (
            [[-5]],
            -2,
            False,
        ),
        (
            [[-1, 3, 5]],
            5,
            True
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.searchMatrix(*case[:-1])
        print(res, case[-1])
