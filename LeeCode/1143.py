class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        子序列不一定是原串中的连续字符
        设 m = len(text1), n = len(text2)
        1. 状态定义
            dp[i][j] : text1[:i] 和 text2[:j] 的最长公共子序列长度
        2. 状态转移
            dp[*][0] = dp[0][*] = 0 其中一个子串为空串，一定没有公共子序列
            对于 i, j
            if text1[i-1] == text2[j-1]:
                # 说明最后一个字符可以加入公共子序列
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # 说明最后一个字符肯定有一个不能加入公共子序列
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


if __name__ == '__main__':
    cases = [
        (
            "abcde", "ace",
            3
        ),
        (
            "abc", "abc",
            3
        ),
        (
            "abc", "def",
            0
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.longestCommonSubsequence(*case[:-1])
        print(res, case[-1])
