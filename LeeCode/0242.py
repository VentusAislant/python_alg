from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        字母异位词即通过相同字符不同排列得到另一个字符串
        所以使用两个哈希表统计词频即可
        """
        if len(s) != len(t):
            return False

        s_counter = defaultdict(int)
        t_counter = defaultdict(int)

        for ch in s:
            s_counter[ch] += 1

        for ch in t:
            t_counter[ch] += 1

        for char, required_num in s_counter.items():
            if char not in t_counter:
                return False
            else:
                if t_counter[char] != required_num:
                    return False
        return True


if __name__ == '__main__':
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
    ]
    solution = Solution()
    for case in cases:
        res = solution.isAnagram(case[0], case[1])
        print(case[2], res)
