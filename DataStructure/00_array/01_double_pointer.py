########################################
# 双指针遍历
########################################
# 双指针遍历，分为两个版本
# 1. 同向双指针，又称快慢指针，可以用于移除重复元素
# 2. 对向双指针，可以用于降低时间复杂度求和，或者回文判断等


# 1. 快慢指针: 移除重复元素. slow之前的元素都是不重复的
arr = [1, 2, 2, 3, 3, 3, 5, 5, 6]
slow = 0
for fast in range(len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]

print(arr)  # [1, 2, 3, 5, 6, 3, 5, 5, 6]
print(arr[:slow + 1])  # [1, 2, 3, 5, 6]

# 2. 对向指针: 求和
arr = range(101)

def comput_sum(arr):
    if len(arr) == 0: return 0

    left, right = 0, len(arr) - 1
    sum_val = 0
    while left < right:
        sum_val += arr[left] + arr[right]
        left += 1
        right -= 1

    # arr 长度是奇数情况
    if left == right:
        sum_val += arr[left]
    return sum_val


print(comput_sum(arr))
