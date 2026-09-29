"""
字符串基本操作
"""

# 字符串的遍历, 可以直接当作数组一样遍历
str_val = "hello"

for i, ch in enumerate(str_val):
    print(i, ch)

for i in range(len(str_val)):
    print(i, str_val[i])

# 切片
str_val = "hello world"
print(str_val[6:])  # world

# 查找
str_val = "hello world"
lowest_idx = str_val.find("world")
print(lowest_idx)  # 6
print(str_val[lowest_idx:lowest_idx+len("world")])
lowest_idx = str_val.find("xxx")  # 找不到会返回 -1
print(lowest_idx)  # -1

lowest_idx = str_val.index("world")
print(lowest_idx)  # 6
# lowest_idx = str_val.index("xxx")  # 找不到会报错 ValueError: substring not found

# 判断是否存在子串
str_val = "hello world"
print('hello' in str_val)  # True
print('xxx' in str_val)  # False