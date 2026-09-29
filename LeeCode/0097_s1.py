class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        记 |s1| = n, |s2| = m
        1. 定义状态
            f(i, j) 表示 s1 的前 i 个元素 和 s2 的前 j 个元素是否能交错组成 s3 的前 i+j 个元素
        2. 递归转移
            如果 s1 的第 i 个元素 和 s3的第 i+j 个元素相等 (最后一个字符相同)，此时
                f(i, j) 取决于 f(i-1, j)
                因为此时 f(i,j)已经用了 s1的最后一个元素，只剩下 s1 的前 i-1 个元素和 s2 的前 j 个元素没用来构成 f(i-1, j)

            如果 s2 的第一个元素和 s3的第 i+j 个元素相等 (最后一个字符相同)，同理

            if s1[i-1] == s3[i+j-1] and f(i-1, j):
                f(i, j) = True
            if s2[j-1] == s3[i+j-1] and f(i, j-1):
                f(i, j) = True
        3. 边界与初始化
            f(0, 0) 表示空字符串可以由空字符串构成
        """

        n, m, k = len(s1), len(s2), len(s3)
        if n + m != k:
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                if j > 0 and s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[n][m]


if __name__ == '__main__':
    cases = [
        (
            "aabcc", "dbbca", "aadbbcbcac",
            True
        ),
        (
            "aabcc", "dbbca", "aadbbbaccc",
            False,
        ),
        (
            "", "", "",
            True
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.isInterleave(*case[:-1])
        print(res, case[-1])
