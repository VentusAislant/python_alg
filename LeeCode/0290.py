class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        双射关系，使用两个哈希表记录 字母和单词的映射
        """
        pattern2s = {}
        s2pattern = {}
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        for ch, word in zip(pattern, s_list):
            if (ch in pattern2s and word != pattern2s[ch]) or \
                    (word in s2pattern and s2pattern[word] != ch):
                return False
            pattern2s[ch] = word
            s2pattern[word] = ch
        return True


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
    ]
    for case in cases:
        res = solution.wordPattern(case[0], case[1])
        print(case[2], res)
