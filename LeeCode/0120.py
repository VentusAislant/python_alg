class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        1. 状态定义：
            用二维数组 dp[i][j] 定义以第 i 层第 j 个结点结尾的最小路径和
        2. 状态转移：
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+ triangle[i][j]
        3. 初始化与边界
            dp[i][j] = inf
            dp[0][0] = triangle[0][0]
        4. 空间优化：
            第 i 行的计算只依赖第 i-1 行，所以空间上只需要一个一维数组即可
        """
        if len(triangle) == 1:
            return triangle[0][0]

        dp = [triangle[0][0]]
        m, n = len(triangle), len(triangle[-1])
        for i in range(1, m):
            row = triangle[i]
            # 扩展一位
            dp.append(float('inf'))
            # 必须从右往左遍历，否则会覆盖掉前面的值
            for j in range(i, -1, -1):  # 第 i 行 有 i+1 个元素
                if j > 0 and j < i:  # 中间的点
                    dp[j] = min(dp[j - 1], dp[j]) + row[j]
                elif j == 0:  # 左端点
                    dp[j] = dp[j] + row[j]
                else:  # 右端点 j=i
                    dp[j] = dp[i - 1] + row[j]

        return int(min(dp))

    def minimumTotalV1(self, triangle: list[list[int]]) -> int:
        """
        1. 状态定义：
            用二维数组 dp[i][j] 定义以第 i 层第 j 个结点结尾的最小路径和
        2. 状态转移：
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+ triangle[i][j]
        3. 初始化与边界
            dp[i][j] = inf
            dp[0][0] = triangle[0][0]
        """
        if len(triangle) == 1:
            return triangle[0][0]

        m, n = len(triangle), len(triangle[-1])
        # dp = [[float('inf')] * n] * m  # 这种写法是错的，因为 * 对于引用类型的对象只复制引用
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0] = [triangle[0][0]]
        for i in range(1, m):
            for j in range(i + 1):  # 第 i 行 有 i+1 个元素
                if j > 0 and j < i:  # 中间的点
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
                elif j == 0:  # 左端点
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                else:  # 右端点 j=i
                    # dp[i - 1][i - 1] 表示上一行右端点
                    dp[i][j] = dp[i - 1][i - 1] + triangle[i][j]

        return int(min(dp[-1]))


if __name__ == '__main__':
    cases = [
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[-10]], -10),
    ]
    solution = Solution()
    for case in cases:
        res = solution.minimumTotal(*case[:-1])
        print(res, case[-1])
