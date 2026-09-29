class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
            productExceptSelfV2 的简单优化
        """
        n = len(nums)
        res = [1] * n  # 先算一次左乘积

        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # 从右往左构建右乘积并乘到 res 上
        right = 1

        # range(start, stop, step), 包含 start 不包含 stop (要到 0 停止，所以设为-1)
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

    def productExceptSelfV2(self, nums: list[int]) -> list[int]:
        """
        左右乘积列表解法：
            引入两个列表，一个列表记录当前元素左侧元素的乘积，一个列表记录当前元素右侧元素的乘积
            最后将两个列表按元素相乘得到最终答案

        时间复杂度 O(N) 空间复杂度O(N)
        """
        left_products = [1]
        right_products = [1]

        tmp = 1
        for i in range(1, len(nums)):
            tmp *= nums[i - 1]
            left_products.append(tmp)

        # 这里可以直接将遍历结果乘到 left_products上来避免额外的数组声明
        tmp = 1
        j = len(nums) - 2
        while j >= 0:
            tmp *= nums[j + 1]
            right_products.append(tmp)
            j -= 1
        right_products.reverse()

        return [l * r for l, r in zip(left_products, right_products)]

    def productExceptSelfV1(self, nums: list[int]) -> list[int]:
        """
        如果有两个或以上 0，则所有元素必为 0
        如果有一个 0，除了0的位置其余位置均为 0
        如果没有 0，每个位置都是整个数组的乘积 / 当前元素值

        时间复杂度 O(N)，空间复杂度 O(1) \
        12ms 22.19MB

        问题：题目中要求不能使用除法，因此不可行
        """
        zero_cnt = 0
        all_product_except_zero = 1
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                all_product_except_zero *= num

        for i in range(len(nums)):
            if zero_cnt >= 2:
                nums[i] = 0
            elif zero_cnt >= 1:
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = all_product_except_zero
            else:
                nums[i] = all_product_except_zero // nums[i]
        return nums


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]
    for case in cases:
        res = solution.productExceptSelf(case[0])
        print(res, case[1])
