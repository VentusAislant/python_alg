class Solution:
    def reverseBits(self, n: int) -> int:
        """
        分治思想，总共 32 位，需要将其逆置，自底向上归并思想
            先将相邻的 bit 交换
            再将相邻的 2-bit 交换
            以此类推

        以 4 bit 数据为例
            0111  -> 10 11 -> 1110
        以 8 bit 数据为例
            01110100 -> 10 11 10 00 -> 1110 0010 -> 00101110

        0x55555555 = 0101 0101 0101 0101 ...
        0x33333333 = 0011 0011 0011 0011 ...
        0x0f0f0f0f = 0000 1111 0000 1111 ...
        0x00ff00ff = 0000 0000 1111 1111 0000 0000 1111 1111
        0x0000ffff = 0000 0000 0000 0000 1111 1111 1111 1111
        """

        n = (n >> 1) & 0x55555555 | (n & 0x55555555) << 1
        n = (n >> 2) & 0x33333333 | (n & 0x33333333) << 2
        n = (n >> 4) & 0x0f0f0f0f | (n & 0x0f0f0f0f) << 4
        n = (n >> 8) & 0x00ff00ff | (n & 0x00ff00ff) << 8
        n = (n >> 16) & 0x0000ffff | (n & 0x0000ffff) << 16
        return n

    def reverseBitsV2(self, n: int) -> int:
        """
        可以通过不断右移，每次取出最后一位，输出即可
        """
        res = 0
        for _ in range(32):
            # n & 1 表示取出 n 的当前最低位
            # res << 1 新增一个最低位
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

    def reverseBitsV1(self, n: int) -> int:
        """
        先转化为二进制字符串（需要补齐32位），然后逆置，再转回二进制字符串
        """
        s = bin(n)[2:]
        s = s.zfill(32)  # 用 0 补齐 32 位
        s = s[::-1]
        return int(s, 2)


if __name__ == '__main__':
    cases = [
        (
            43261596,
            964176192
        ),
        (
            2147483644,
            1073741822
        ),
    ]
    solution = Solution()
    for case in cases:
        res = solution.reverseBits(*case[:-1])
        print(res, case[-1])
