class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        双向指针，因为元素的顺序和右指针后的元素不重要, 左指针前的所有元素均为其他元素
        """
        i, j = 0, len(nums) - 1

        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
                # 更换表尾元素后左指针不右移，因为表尾元素仍可能是 val
            else:
                i += 1

        return j + 1  # j始终指向最后一个有效元素
