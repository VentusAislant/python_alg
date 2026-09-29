class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        首先统计 wordDict 中可能的单词长度 word_len = []
        dp[i] 表示前i个字符是否存在单词切分
        如果存在 j < i, 使 dp[j] = True 且 s[j:i] 在 wordDict 中，则
            dp[i] = True
        否则 dp[i] = False
        """
        word_len = []
        for word in wordDict:
            if len(word) not in word_len:
                word_len.append(len(word))

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # dp[0] 表示 s 中的前0个字符能否被单词切分，空字符串是不影响单词切分的，可以认为已经切分
        for i in range(1, n + 1):
            for l in word_len:
                if i - l >= 0 and dp[i - l] and s[i - l:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == '__main__':
    cases = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ]
    solution = Solution()
    for case in cases:
        res = solution.wordBreak(*case[:-1])
        print(res, case[-1])
