class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        每个字符串设置一个指针，根据 s 的指针的值来移动 t 的指针
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ('abc', 'ahbgdc', True),
        ("axc", "ahbgdc", False),
    ]
    for case in cases:
        result = solution.isSubsequence(case[0], case[1])
        print(result, case[2])
