class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        无论如何先选一个数字，再确定两个数字，至少用到 O(n^2) 时间，因此可以先排序
        先排序，先选定一个数字，可以是下标 i=[0, n-2)
            然后剩下的两个数从 nums[i:]找，此时可以利用找两个数的和的算法来找
            使用双指针分别指向两端，当和较小左指针右移动，当和较大右指针左移
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                # 和前面先选的数相同，直接跳过即可
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 跳过重复元素
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
        return res


if __name__ == '__main__':
    cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]])
    ]
    solution = Solution()
    for case in cases:
        result = solution.threeSum(case[0])
        print(result, case[1])