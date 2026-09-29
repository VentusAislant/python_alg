class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        先二分查找行坐标，再二分查找列坐标
        """
        row_l, row_r = 0, len(matrix)
        col_l, col_r = 0, len(matrix[0])

        while row_l < row_r:
            mid = (row_l + row_r) >> 1
            if matrix[mid][0] <= target:
                row_l = mid + 1
            else:
                row_r = mid

        while col_l < col_r:
            mid = (col_l + col_r) >> 1
            if matrix[row_l - 1][mid] <= target:
                col_l = mid + 1
            else:
                col_r = mid

        return matrix[row_l - 1][col_l - 1] == target


if __name__ == '__main__':
    cases = [
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3,
            True
        ),
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13,
            False
        ),
    ]
    solution = Solution()
    for case in cases:
        res = solution.searchMatrix(*case[:-1])
        print(res, case[-1])
