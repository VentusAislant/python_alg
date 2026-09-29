class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """
        一个片段是否合法，需要这个片段覆盖每个字母出现的最后的位置
        所以可以用一个哈希表记录每个字母出现的最后的位置
        然后遍历字符串，动态维护区间 start, end
            如果当前片段出现了一个新的字符，必须覆盖其最后一次出现的位置

        ababcc
        i = 0 -> end = 2
        i = 1 -> end = 3
        i = 2 -> end = 3
        i = 3 -> end = 3  -> res.append(3-0+1=4), start=4
        i = 4 -> end = 5
        i = 5 -> end = 5  -> res.append(5-4+1=2)
        """
        last_pos = {}
        for idx, char in enumerate(s):
            last_pos[char] = idx

        res = []
        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last_pos[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res


if __name__ == '__main__':
    cases = [
        (
            "ababcbacadefegdehijhklij",
            [9, 7, 8]
        ),
        (
            "eccbbbbdec",
            [10]
        )
    ]
    solution = Solution()
    for case in cases:
        solution.partitionLabels(case[0])
        res = case[0]
        print(res, case[-1])
