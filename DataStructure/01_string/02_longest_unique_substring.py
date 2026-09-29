"""
找最长不重复字串
"""

def length_of_longest_substring(s):
    window = list()  # 记录当前窗口中出现的字符
    left = 0  # 当前窗口的左边界
    max_len = 0  # 最终的最长子串长度
    final_str = ""
    for idx, right in enumerate(range(len(s))):
        while s[right] in window:  # 只要当前窗口有重复的字符，就不断右移窗口的左边界
            window.remove(s[left])
            left += 1
        window.append(s[right])
        if right - left + 1 > max_len:
            final_str = s[left:right + 1]
            max_len = right - left + 1
    return max_len, final_str


print(length_of_longest_substring("abacdefaacabcdbb"))
