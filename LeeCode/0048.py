class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        矩阵比较好实现的操作是转置，但是转置后和旋转图像有细微差异，只需要每一行进行翻转即可
        1 2 3       1 4 7       7 4 1
        4 5 6  ---> 2 5 8  ---> 8 5 2
        7 8 9       3 6 9       9 6 3
        """
        # 先转置
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 水平翻转没一行
        for row in matrix:
            row.reverse()


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
         [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
    ]
    for case in cases:
        s.rotate(case[0])
        print(case[0], case[1])
