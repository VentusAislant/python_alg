class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        简单解法： 依次往后判断每个字符串的相同位置的元素是否相同
        """
        pos = 0
        min_len = min([len(s) for s in strs])
        while pos < min_len:
            cur_str = strs[0][pos]
            can_continue = True
            for i in range(1, len(strs)):
                if strs[i][pos] != cur_str:
                    can_continue = False
                    break
            if can_continue:
                pos += 1
            else:
                break
        return strs[0][:pos]





if __name__ == '__main__':
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ]
    s = Solution()

    for (input, answer) in test_cases:
        my_answer = s.longestCommonPrefix(input)
        print(my_answer, answer)
