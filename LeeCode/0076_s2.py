from collections import Counter, defaultdict


class Solution:
    @staticmethod
    def check(window, need):
        """
        检查当前窗口是否覆盖了 t 所需全部字符
        """
        # need 中每个字符都必须满足：window[c] >= need[c]
        for char, num_required in need.items():
            if window[char] < num_required:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        """
        简单解法，遍历 s 中所有长度从 len(t) 到 len(d) 的子串，判断是否符合条件，会超时 O(mn)

        滑动窗口解法:
            我们在 s 上滑动窗口，通过移动 r 指针不断扩张窗口。
            当窗口包含 t 全部所需的字符后，如果我们能收缩，我们就收缩窗口知道得到最小窗口
        """

        # need：记录 t 中每个字符需要出现的次数
        need = defaultdict(int)
        for c in t:
            need[c] += 1

        # window：当前窗口中对应字符出现次数
        window = defaultdict(int)

        # 左边界 l，右边界 r（注意 r 初始为 -1，表示窗口为空）
        l, r = 0, -1

        # 最小窗口的长度和位置
        min_len = float('inf')
        ans_l, ans_r = -1, -1

        # 主循环——右指针不断右移
        while r < len(s):
            r += 1  # 扩张右边界

            # 若新加入窗口的字符在 need 字符中，则计数增加
            if r < len(s) and s[r] in need:
                window[s[r]] += 1

            # 当窗口已经满足“包含全部 t 的字符及其次数”，尝试收缩左边界
            while self.check(window, need) and l <= r:
                # 更新最小窗口
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans_l = l
                    ans_r = l + min_len  # Python 切片用右开区间

                # 左指针准备右移：把即将移出窗口的字符频次减少
                if s[l] in need:
                    window[s[l]] -= 1

                l += 1

        # 如果没有找到有效窗口
        return "" if ans_l == -1 else s[ans_l:ans_r]


if __name__ == '__main__':
    cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", "")
    ]

    solution = Solution()
    for case in cases:
        my_answer = solution.minWindow(*case[:-1])
        print(my_answer, case[-1])
