class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        直接使用一个行指针，在行之间上下摆动
        时间复杂度 O(N)   空间复杂度 O(N)
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cur_row = 0
        step = 1  # 向下走表示 1， 向上走表示 -1

        for c in s:
            rows[cur_row] += c
            # 更新方向
            if cur_row == 0:
                step = 1
            elif cur_row == numRows - 1:
                step = -1

            cur_row += step
        return ''.join(rows)

    def convertV1(self, s: str, numRows: int) -> str:
        """
        简单算法：按列填充矩阵，每列填充有一定规律
            对于 col % (numRows - 1): 顺序填充 numRows 个
            对于 col % (numRows - 1) == i, 填充 numRows - i  - 1 个空格，再填充一个字符，再填充 i 个空格

            由于题目中没有要求最终打印，所以无需填充空格
            时间复杂度 O(N)   空间复杂度 O(N)
        """
        if numRows == 1:
            return s

        matrix = ['' for _ in range(numRows)]
        cur_col = 0
        i = 0
        while i < len(s):
            if cur_col % (numRows - 1) == 0:
                for j in range(numRows):
                    if i < len(s):
                        matrix[j] += s[i]
                        i += 1
            else:
                k = cur_col % (numRows - 1)
                j = 0
                while j < numRows - k - 1:
                    matrix[j] += ' '
                    j += 1

                matrix[j] += s[i]
                j += 1
                i += 1

                while j < numRows:
                    matrix[j] += ' '
                    j += 1
            cur_col += 1
        return ''.join([c for s in matrix for c in s if not str(c).isspace()])


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
        ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
        ('A', 1, 'A')
    ]
    for s, numRows, gt in cases:
        result = solution.convert(s, numRows)
        print(result, gt)
