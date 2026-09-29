class Solution:
    """
    还可以使用 KMP 字符串匹配算法
    """
    def strStr(self, haystack: str, needle: str) -> int:
        """
        暴力匹配，直接从 haystack 中找所有长度和 needle 长度相同的所有子串匹配一次
        时间复杂度 O(M*N)
        """
        m, n = len(needle), len(haystack)
        for i in range(0, n - m + 1):
            if haystack[i: i + m] == needle:
                return i
        return -1

    def strStrV1(self, haystack: str, needle: str) -> int:
        """
        Python 中内置的算法 str.find() 当找不到子串则返回-1
        如果使用 str.index() 找不到子串会报错
        """
        return haystack.find(needle)


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
    ]
    for case in cases:
        result = solution.strStr(*case[:-1])
        print(result, case[-1])
