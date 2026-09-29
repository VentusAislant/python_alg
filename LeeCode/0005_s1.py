class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        1. 状态定义：
            用二维数组 dp[i][j] 表示 s[i:j+1] 子串的是否是回文串， 用一个额外变量维护最长长度和开始索引
        2. 状态转移：
            当前长度为 1 (i==j)
                dp[i][j] = True
            当前长度为 2 (j-i = 1)
                dp[i][j] = s[i] == s[j]
            当前长度为 3 (j-i == 2)
                dp[i][j] = s[i] == s[j]
            当前长度为 4 (j-i == 3)
                dp[i][j] = s[i] == s[j] and dp[i-1][j-1]
            当前长度为 5 (j -i==4)
                dp[i][j] = s[i] == s[j] and dp[i-1][j-1]
            ...

            因此
            if j-i == 0:
                dp[i][j] = True
            elif j-i <= 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

            由于计算 d[i][j] 用到了 dp[i+1][j-1], 所以遍历时候 i 需要从后往前，j需要从前往后
        3. 初始化与边界
            上面的式子包含初始化
        """
        max_len = 0
        start_pos = -1
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i == 0:
                    dp[i][j] = True
                elif j - i <= 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start_pos = i

        return s[start_pos:start_pos + max_len]


if __name__ == '__main__':
    cases = [
        (
            "babad",
            "bab"
        ),
        (
            "cbbd",
            "bb"
        ),
        (
            "aaaa",
            "aaaa"
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.longestPalindrome(*case[:-1])
        print(res, case[-1])
