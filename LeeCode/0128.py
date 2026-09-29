class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        可以发现，我们可以通过在哈希表判断 x-1 是否存在，来确定当前点是否是一个连续序列的起点
        因此可以避免左右扩展，还可以避免用 seen 来记录访问过的元素
        每次只从起点开始访问，访问每个可能的序列，例如
        [100, 1, 2, 101, 3, 4]
        只需要从 100 开始 和 1开始即可

        时间复杂度 O(N)
        空间复杂度 O(N)
        """
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                # 是起点
                cur = num
                cur_len = 1
                while cur + 1 in nums:
                    cur += 1
                    cur_len += 1
                if cur_len > res:
                    res = cur_len
        return res

    def longestConsecutiveV2(self, nums: list[int]) -> int:
        """
        将 nums 转化为哈希表，然后一次判断，如果遇到过则可记录长度并向后判断
        如何优化 V1 版本，可以看出 V1版本会有很多重复计算，例如
        [1, 2, 3, 4]， 针对每个元素都要遍历一边来获得每个元素的最大连续长度，其实他们都属于同一个
        所以可以用一个 seen 哈希表记录访问过的元素，避免重复

        时间复杂度 O(N)
        空间复杂度 O(N)
        """
        nums = set(nums)
        seen = set()
        res = 0
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            cur_num = num
            cur_len = 1
            while cur_num + 1 in nums:
                cur_len += 1
                cur_num += 1
                seen.add(cur_num)

            cur_num = num
            while cur_num - 1 in nums:
                cur_len += 1
                cur_num -= 1
                seen.add(cur_num)

            if cur_len > res:
                res = cur_len
        return res

    def longestConsecutiveV1(self, nums: list[int]) -> int:
        """
        将 nums 转化为哈希表，然后一次判断，如果遇到过则可记录长度并向后判断


        时间复杂度 O(N^2)
        空间复杂度 O(N)
        """
        nums = set(nums)
        res = 0
        for num in nums:
            cur_num = num
            cur_len = 1
            while cur_num + 1 in nums:
                cur_len += 1
                cur_num += 1

            cur_num = num
            while cur_num - 1 in nums:
                cur_len += 1
                cur_num -= 1

            if cur_len > res:
                res = cur_len
        return res


if __name__ == '__main__':
    cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
    ]
    solution = Solution()
    for case in cases:
        res = solution.longestConsecutive(case[0])
        print(res, case[1])
