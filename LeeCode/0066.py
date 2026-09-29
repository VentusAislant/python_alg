class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        先在个位上+1，然后进位即可
        为什么不能转成 int 再加，因为可能数值溢出，假设list特别长超过32，这个相加就会溢出
        """
        digits[-1] += 1
        i = len(digits) - 1
        while i >= 0:
            if i > 0 and digits[i] >= 10:
                # 需要向前进位
                digits[i] -= 10
                digits[i - 1] += 1
            elif i == 0 and digits[i] >= 10:
                # 已经到了最高位，还需要向前进位，则直接在最开始添加一个1
                digits[0] -= 10
                digits.insert(0, 1)
            else:
                break
            i -= 1
        return digits


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
    ]
    for case in cases:
        res = s.plusOne(*case[:-1])
        print(res, case[-1])
