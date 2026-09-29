class Solution:
    def intToRoman(self, num: int) -> str:
        map = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        res = ''
        while num > 0:
            for k, v in map.items():
                if num >= v:
                    res += k
                    num -= v
                    break
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (3749, 'MMMDCCXLIX'), (58, 'LVIII'), (1994, 'MCMXCIV')
    ]
    for input, answer in cases:
        print(answer, solution.intToRoman(input))
