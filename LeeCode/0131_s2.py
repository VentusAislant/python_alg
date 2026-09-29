class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        采用动态规划判断子串是否为回文串， 这样避免在回溯的时候每次用O(n)时间检查是否为回文串
        dp[i][j] 表示 s[i:j+1] 是否为回文串则有
            if i >= j: dp[i][j] = True  空串和单个字符的串默认是回文串
            d[i][j] = d[i+1, j-1] and s[i]==s[j]  这里i依赖于 i+1，j依赖于j-1，所以 i需要从 n-1遍历到0
        采用回溯来遍历所有分割情况
            递归终止条件： i=n 表示所有字符已经切分完，当前切法是一种解
            路径解析： 对于 aab
            i=0
             ├─ j=0 → "a"
             │   i=1
             │    ├─ j=1 → "a"
             │    │   i=2
             │    │    └─ j=2 → "b" → ✓
             │    └─ j=2 ×
             └─ j=1 → "aa"
                 i=2
                  └─ j=2 → "b" → ✓


        时间复杂度 O(n*2^n)
        空间复杂度 O(n^2)
        """
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            # 因为先确定 i>=j 的位置的值，所以 i 要从大往小遍历
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        res = []
        cur_ans = []

        def dfs(i):
            if i == n:
                res.append(cur_ans[:])
                return
            for j in range(i, n):
                if dp[i][j]:
                    cur_ans.append(s[i:j + 1])
                    dfs(j + 1)
                    cur_ans.pop()

        dfs(0)
        return res


if __name__ == '__main__':
    cases = [
        (
            "aab",
            [["a", "a", "b"], ["aa", "b"]]
        ),
        (
            "a",
            [["a"]]
        ),
    ]
    solution = Solution()
    for case in cases:
        res = solution.partition(*case[:-1])
        print(res, case[-1])
