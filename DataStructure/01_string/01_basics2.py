"""
字符串的替换 (可以链式调用)
"""
str_val = 'model.mm_projector.weight'
new_str_val = str_val.replace('model.', '').replace('mm_projector', 'projector')
print(new_str_val)  # projector.weight

"""
字符串的拆分与拼接
"""
str_val = 'hello, I am Rose'
word_lst = str_val.split(' ')
print(word_lst)  # ['hello,', 'I', 'am', 'Rose']

new_str_val = ' '.join(word_lst)
print(new_str_val)  # hello, I am Rose

ch_lst = list(str_val)
print(ch_lst) # ['h', 'e', ..., 'R', 'o', 's', 'e']

"""
判断字符串类型
"""
# 判断字符串类型
# isdigit() 是否全是数字
# isalpha() 是否全是字母(不包含空格和标点符号)
# isalnum() 是否全是数字或者字母
# isspace()	是否全是空白字符（空格、换行）
# islower()	是否全是小写字母
# isupper()	是否全是大写字母

examples = ["abc", "ABC", "123", "abc123", "abc!", "\n", "abc DEF", 'こんにちは']

for s in examples:
    print(f"'{s}': isdigit={s.isdigit()}, isalpha={s.isalpha()}, isalnum={s.isalnum()}, isspace={s.isspace()}")

"""
'abc': isdigit=False, isalpha=True, isalnum=True, isspace=False
'ABC': isdigit=False, isalpha=True, isalnum=True, isspace=False
'123': isdigit=True, isalpha=False, isalnum=True, isspace=False
'abc123': isdigit=False, isalpha=False, isalnum=True, isspace=False
'abc!': isdigit=False, isalpha=False, isalnum=False, isspace=False
'\n': isdigit=False, isalpha=False, isalnum=False, isspace=True
'abc DEF': isdigit=False, isalpha=False, isalnum=False, isspace=False
'こんにちは': isdigit=False, isalpha=True, isalnum=True, isspace=False
"""

"""
字符串大小写转化
"""
str_val = 'HeLLo WORld'

print(str_val.lower())  # hello world
print(str_val.upper())  # HELLO WORLD
print(str_val.capitalize())  # Hello world

"""
使用 collections.Counter 快速统计词频
"""
from collections import Counter

str_val = 'abcabcabcaaabbbccc'
count = Counter(str_val)
print(count)  # Counter({'a': 6, 'b': 6, 'c': 6})

str_lst = ['aaa'] * 5 + ['bbb'] * 10 + ['ccc'] * 100
count = Counter(str_lst)
print(count)  # Counter({'ccc': 100, 'bbb': 10, 'aaa': 5})
