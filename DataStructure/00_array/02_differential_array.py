"""
差分数组是一种可以快速对原数组某个区间进行加/减操作的技巧。它把原数组的“变化量”提取出来进行处理。
"""

arr = [5, 7, 7, 9, 10]


# 差分数组的构建
def build_diff_arr(arr):
    diff_arr = [arr[0]]
    for i in range(1, len(arr)):
        diff_arr.append(arr[i] - arr[i - 1])
    return diff_arr


diff_arr = build_diff_arr(arr)
print(diff_arr)  # [5, 2, 0, 2, 1]


# 差分数组的恢复
def restore_arr(diff_arr):
    arr = [diff_arr[0]]
    for i in range(1, len(diff_arr)):
        arr.append(arr[i - 1] + diff_arr[i])
    return arr


arr = restore_arr(diff_arr)
print(arr)  # [5, 7, 7, 9, 10]


# 对区间进行数值加/减的数值更新, 实际索引为 i -> j-1
def update_range(diff_arr, i, j, val):
    diff_arr[i] += val
    if j <= len(diff_arr):
        diff_arr[j] -= val


update_range(diff_arr, 1, 3, 10)
print(diff_arr)  # [5, 2, 0, 2, 1] -> [5, 12, 0, -8, 1]
arr = restore_arr(diff_arr)
print(arr)  # [5, 17, 17, 9, 10]
