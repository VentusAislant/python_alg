class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': (1, 1),
            'V': (5, 2),
            'X': (10, 3),
            'L': (50, 4),
            'C': (100, 5),
            'D': (500, 6),
            'M': (1000, 7)
        }

        res = 0
        i = 0
        while i < len(s):
            # 对于 I X C 存在六种特殊情况
            if i < len(s) - 1 and (s[i] == 'I' or s[i] == 'X' or s[i] == 'C'):
                if 1 <= roman_dict[s[i+1]][1] - roman_dict[s[i]][1] <= 2:
                    res += roman_dict[s[i+1]][0] - roman_dict[s[i]][0]
                    i += 2
                    continue
            res += roman_dict[s[i]][0]
            i += 1
        return res


if __name__ == '__main__':
    test_cases = [
        'III', 'IV', 'IX', 'LVIII', 'MCMXCIV'
    ]
    answers = [
        3, 4, 9, 58, 1994
    ]

    s = Solution()

    for test_case, answer in zip(test_cases, answers):
        my_answer = s.romanToInt(test_case)
        print(my_answer, answer)
