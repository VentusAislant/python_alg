class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        标准的快慢指针，慢指针左侧是不重复元素
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])
    ]
    for case in cases:
        r = s.removeDuplicates(case[0])
        print('M: ', case[0][:r])
        print('A: ', case[1])
