"""
- 数组内置排序
    - Python的内置排序利用的是稳定的排序算法，结合了归并排序和插入排序
"""

# 数组原地排序, 返回值为None，直接修改当前数组
arr = [1, 3, 5, 7, 8, 2, 4]
arr.sort()
print(arr)  # [1, 2, 3, 4, 5, 7, 8]


# 排序后返回新的数组，不改变原数组
arr = [1, 3, 5, 7, 8, 2, 4]
sorted_arr = sorted(arr)
print(arr)  # [1, 3, 5, 7, 8, 2, 4]
print(sorted_arr)  # [1, 2, 3, 4, 5, 7, 8]

# 两种排序方式的逆序排序版本（降序）
arr = [1, 3, 5, 7, 8, 2, 4]
arr.sort(reverse=True)
print(arr)  # [8, 7, 5, 4, 3, 2, 1]

arr = [1, 3, 5, 7, 8, 2, 4]
sorted_arr = sorted(arr, reverse=True)
print(arr)  # [1, 3, 5, 7, 8, 2, 4]
print(sorted_arr)  # [8, 7, 5, 4, 3, 2, 1]