class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        使用两个哈希表来记录映射关系，因为这个映射是双向的（双射），遍历 s 和 t
        """
        map_st = {}
        map_ts = {}
        for ch_s, ch_t in zip(s, t):
            if (ch_s in map_st and map_st[ch_s] != ch_t) or \
                    (ch_t in map_ts and map_ts[ch_t] != ch_s):
                return False
            map_st[ch_s] = ch_t
            map_ts[ch_t] = ch_s
        return True


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ('egg', 'add', True),
        ('foo', 'bar', False),
        ('paper', 'title', True),
        ("badc", "baba", False),
    ]
    for case in cases:
        res = solution.isIsomorphic(case[0], case[1])
        print(case[2], res)
