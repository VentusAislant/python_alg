class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        深度优先遍历 + 回溯，只遍历一遍得到结果, 使用 idx 记录当前遍历的位置，可以直接和 word 匹配来减枝,
        此外也无需 visited 来记录访问结点，直接在棋盘上用其他符号标记即可，回溯的时候复原
        """
        m = len(board)
        n = len(board[0])

        def dfs(node, idx=0) -> bool:
            x, y = node

            # 当前字符不匹配，直接结束
            if word[idx] != board[x][y]:
                return False

            # 已经匹配到最后一个字符
            if idx == len(word) - 1:
                return True

            tmp = board[x][y]
            board[x][y] = '#'  # 标记访问
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '#':
                    if dfs((nx, ny), idx + 1):
                        return True
            # 回溯
            board[x][y] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if dfs((i, j)):
                    return True
        return False

    def existV1(self, board: list[list[str]], word: str) -> bool:
        """
        深度优先遍历 + 回溯，只遍历一遍得到结果
        这种做法目前会每次深度遍历到底，不知道提前结束，假如 word=SEE
        目前得到的是 ABC 但是不会结束还是会深度遍历到所有结点
        """
        m = len(board)
        n = len(board[0])

        def dfs(node, visited, cur_word="") -> bool:
            x, y = node
            visited.add((x, y))
            cur_word += board[x][y]
            if cur_word == word:
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if dfs((nx, ny), visited, cur_word):
                        return True
            # 回溯
            visited.remove(node)
            return False

        for i in range(m):
            for j in range(n):
                if dfs((i, j), set()):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED",
            True
        ),
        (
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE',
            True
        ),
        (
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB',
            False
        ),
        (
            [["a", "b"], ["c", "d"]], "cdba",
            True
        )
    ]
    for case in cases:
        res = solution.existV1(*case[:-1])
        print(res, case[-1])
