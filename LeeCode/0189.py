class Solution:
    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        轮转 k 个位置等于，先逆置数组，再逆置前k个数，再逆置后n-k个
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        return None

    def rotateV2(self, nums: list[int], k: int) -> None:
        """
        轮转 k 个位置等于，先逆置数组，再逆置前k个数，再逆置后n-k个
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return None

    def rotateV1(self, nums: list[int], k: int) -> None:
        """
        使用额外数组存储后面 k 个元素来辅助轮转
        """
        k = k % len(nums)
        if k < 1:
            return None
        tmp_lst = nums[-k:]
        for i in reversed(range(0, len(nums) - k)):
            nums[i + k] = nums[i]
        nums[:k] = tmp_lst
        return None


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
        (([-1, -100, 3, 99], 2), [3, 99, -1, -100])
    ]
    for case in cases:
        solution.rotate(*case[0])
        print(case[0][0], case[1])
