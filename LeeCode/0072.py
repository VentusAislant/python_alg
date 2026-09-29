class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        对于字符串操作，动态规划往往通过前缀来实现
        1. 定义状态
            dp[i][j] 表示 把 word1 的前 i 个字符变成 word2 的前 j 个字符所需要的最少操作数
        2. 状态转移
            对于 i,j
            如果 word[i-1] == word[j-1], 最后一个字符相同，什么都不用做
                dp[i][j] = dp[i-1][j-1]
            如果最后一个字符不同，则必须选三种操作之一
                删除 word1 的第 i-1 个字符
                    dp[i][j] = dp[i-1][j] + 1
                在 word1 中插入 word2[j-1]
                    dp[i][j] = dp[i][j-1] + 1
                将 word1[i-1] 替换成 word2[j-1]
                    dp[i][j] = dp[i-1][j-1] + 1
        3. 初始化
            dp[i][0] = i  需要删除 i 次
            dp[0][j] = j  需要删除 j 次
        """
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # 删除
                        dp[i][j - 1] + 1,  # 插入
                        dp[i - 1][j - 1] + 1  # 替换
                    )

        return dp[n][m]


if __name__ == '__main__':
    cases = [
        (
            "horse", "ros",
            3
        ),
        (
            "intention", "execution",
            5
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.minDistance(*case[:-1])
        print(res, case[-1])
