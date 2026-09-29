from collections import defaultdict


class Solution:
    def canConstruct(self, randomNote: str, magazine: str) -> bool:
        """
        使用两个哈希表，一个存储 randomNote 的字符频率，一个存储 magazine 的字符频率
            然后对比字符频率，确保 randomNote 的每个字符频率都小于等于 magazine 的
        """
        randomNote_counter = defaultdict(int)
        magazine_counter = defaultdict(int)
        for char in randomNote:
            randomNote_counter[char] += 1

        for char in magazine:
            magazine_counter[char] += 1

        for char, required_num in randomNote_counter.items():
            if char not in magazine_counter:
                return False
            else:
                if required_num > magazine_counter[char]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ('a', 'b', False),
        ('aa', 'ab', False),
        ('aa', 'aab', True),
    ]
    for case in cases:
        res = solution.canConstruct(case[0], case[1])
        print(case[2], res)
