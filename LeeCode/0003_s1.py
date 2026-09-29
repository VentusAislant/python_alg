class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        最简单的做法还是遍历所有起点开始的，所有长度的子串

        改进：滑动窗口
        用 left 和 right 记录当前窗口，利用一个 set 来保证窗口中没有重复字符， 同时实时记录最长子串长度
            1. right 每次向右扩展一个字符
            2. 如果字符已经出现在窗口，则移动 left 到重复字符的右边，保证窗口仍无重复元素
            3. 不断更新当前最长子串
        """
        seen = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            res = max(res, right - left + 1)
        return res


if __name__ == '__main__':
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]

    solution = Solution()
    for input, answer in cases:
        result = solution.lengthOfLongestSubstring(input)
        print(answer, result)
