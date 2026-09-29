from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        首先记录 p 中的字符次数统计，然后对 s 进行滑动窗口，如果窗口满足要求则压入其实元素到结果中，
        同时用一个哈希表来存储当前窗口中的字符统计，从而来动态计算
        """
        if len(p) > len(s):
            return []

        target = defaultdict(int)
        for c in p:
            target[c] += 1

        res = []
        cur = defaultdict(int)
        l, r = 0, 0
        while r < len(s):
            cur[s[r]] += 1

            # 如果窗口长度超过 p 的长度，必须收缩窗口
            if r - l + 1 > len(p):
                cur[s[l]] -= 1
                if cur[s[l]] == 0:
                    del cur[s[l]]
                l += 1

            if r - l + 1 == len(p) and cur == target:
                res.append(l)
            r += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            "cbaebabacd", "abc",
            [0, 6]
        ),
        (
            "abab", "ab",
            [0, 1, 2]
        )
    ]
    for case in cases:
        res = solution.findAnagrams(*case[:-1])
        print(res, case[-1])
