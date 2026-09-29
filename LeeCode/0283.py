class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        双指针思想, p1 前面全是有序的非 0 元素， p2 后面都是不要的元素
        移动 p2 使得
            [0, p1) 全是已经处理好的原序的非 0 元素
            [p1, i) 已经处理过，但目前可以是不要的值
            [i, n) 尚未处理
        以 [9, 0, 1, 0, 3, 12] 为例
        p1=0, p2=0 => [9, 0, 1, 0, 3, 12]
        p1=1, p2=1 => [9, 0, 1, 0, 3, 12]
        p1=1, p2=2 => [9, 1, 0, 0, 3, 12]
        p1=2, p2=3 => [9, 1, 0, 0, 3, 12]
        p1=2, p2=4 => [9, 1, 3, 0, 0, 12]
        p1=3, p2=5 => [9, 1, 3, 12, 0, 0]
        p1=3, p2=6 => end
        """
        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0])
    ]
    for case in cases:
        solution.moveZeroes(case[0])
        print(case[0], case[1])
