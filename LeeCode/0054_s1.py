class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        螺旋遍历：
            想象有最外围有四条线，分别记作 top, right, bottom, left
            沿着当前线进行遍历，遍历完毕后，线向相反方向移动即可
        """
        res = []
        m, n = len(matrix), len(matrix[0])
        top, right, bottom, left = 0, n-1, m-1, 0
        while left <= right and top <= bottom:
            # 沿着 top 线，从左往右遍历
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            # top 线下移
            top += 1
            if top > bottom: break  # ✅ 防止越界

            # 沿着 right 线，从上往下遍历
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right: break  # ✅ 防止越界

            # 沿着 bottom 线，从右往左遍历
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom: break  # ✅ 防止越界

            # 沿着 left 线，从下往上遍历
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        )
    ]
    for case in cases:
        result = solution.spiralOrder(case[0])
        print(result, case[1])
