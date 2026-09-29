class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """
        扬辉三角
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for i in range(2, numRows):
            new_row = [1]
            for j in range(1, i):
                new_row.append(res[i-1][j - 1] + res[i-1][j])
            new_row.append(1)
            res.append(new_row)
        return res


if __name__ == '__main__':
    cases = [
        (
            5,
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        ),
        (
            1,
            [[1]]
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.generate(*case[:-1])
        print(res, case[-1])
