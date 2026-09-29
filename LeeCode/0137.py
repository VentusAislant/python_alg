class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        要求时间复杂度 O(N) 空间复杂度 O(1)
        因为元素要么只出现一次，要么就出现三次
        假设有一个数组统计所有数的二进制的每个位的 1 的个数
            [3, 3, 3, 2, 2, 2, 5]
            3 = 011  2=010  5=101
            此时 bit_cnt = [1,6,4], %3 后 [1, 0, 1] 也就是最终答案
        如何避免使用数组来统计每个bit的1的个数呢？可以直接通过从低位到高位遍历bit 位，同时记录答案
        """
        res = 0
        for i in range(32):
            # 遍历第 i 个二进制位置，0表示最低位
            bit_cnt = 0
            for x in nums:
                bit_cnt += (x >> i) & 1

            if bit_cnt % 3 != 0:
                res = res | (1 << i)  # 在 res 对应位上添加一个 1

        # 负数情况
        if res >= 2 ** 31:
            res -= 1 << 32  # 把最高位的 1 消除

        return res


if __name__ == '__main__':
    cases = [
        (
            [2, 2, 3, 2],
            3
        ),
        (
            [0, 1, 0, 1, 0, 1, 99],
            99
        ),
        (
            [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2],
            -4
        )
    ]
    solution = Solution()
    for case in cases:
        res = solution.singleNumber(*case[:-1])
        print(res, case[-1])
