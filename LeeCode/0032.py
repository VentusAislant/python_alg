class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        在每个 ) 位置，判断它能不能和前面的某个 ( 匹配，
        如果能，就把中间和前面的有效长度全部接起来。

        最长有效括号
            dp[i]: 表示 s[:i+1] 的最长有效括号子串长度

            if s[i] == '(':
                dp[i] = 0  # 不可能形成有效括号子串
            else:
                # 右括号，可能增加子串长度
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                else:
                    j = i - dp[i-1] - 1  # 找到前面第一个没匹配的符号
                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i-1] + 2 + (dp[j - 1] if j >= 1 else 0)
                res = max(res, dp[i])
        """
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
            else:
                # 右括号，可能增加子串长度
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                else:
                    j = i - dp[i - 1] - 1  # 找到前面第一个没匹配的符号
                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)
                res = max(res, dp[i])
        return res


if __name__ == '__main__':
    cases = [
        (
            "(()",
            2
        ),
        (
            ")()())",
            4
        ),
        (
            "",
            0
        ),
        (
            "()(()",
            2
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.longestValidParentheses(*case[:-1])
        print(res, case[-1])
