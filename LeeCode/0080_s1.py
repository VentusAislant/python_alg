class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        首先数组是有序的，所有相同元素都挨在一起
        用一个指针 i 表示 下一个可写入的位置
        遍历数组时，对于每个 num
            如果 i < 2, 直接写入
            否则，如果 nums[i-2] != num, 说明这个数最多只出现了1次，可以写入第2个
            如果相等，则说明之前已经写过两次，直接跳过
        """
        i = 0
        for num in nums:
            if i < 2 or nums[i-2] != num:
                nums[i] = num
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3])
    ]
    for case in cases:
        r = s.removeDuplicates(case[0])
        print('M: ', case[0][:r])
        print('A: ', case[1])
