class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        """
        四叉树用来标识矩形块中哪块是全0或全1，用分治的思想，将当前矩阵分成四块递归判断
            如果四个子块全是 leaf 并且 val 相同，则当前为一整个子块
            否则当四个子块是一个父结点，有四个孩子
        """

        def _construct(i, j, length) -> Node | None:
            """
            i， j 表示左上角坐标，length 标识当前块长尺寸
            """
            if length == 1:
                # 只有一格
                return Node(grid[i][j], True, None, None, None, None)

            half = length // 2

            tl = _construct(i, j, half)
            tr = _construct(i, j + half, half)
            bl = _construct(i + half, j, half)
            br = _construct(i + half, j + half, half)

            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True, None, None, None, None)

            return Node(0, False, tl, tr, bl, br)

        return _construct(0, 0, len(grid))


def get_level_order(root: Node) -> list[list[int] | None]:
    from collections import deque
    queue = deque([root])
    level_order = []
    while queue:
        node = queue.popleft()
        if node:
            level_order.append([int(node.isLeaf), node.val])
            queue.append(node.topLeft)
            queue.append(node.topRight)
            queue.append(node.bottomLeft)
            queue.append(node.bottomRight)
        else:
            level_order.append(None)

    while level_order and level_order[-1] is None:
        level_order.pop()

    return level_order


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [[0, 1], [1, 0]],
            [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
        ),
        (
            [
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0]
            ],
            [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]
        )
    ]
    for case in cases:
        tree = solution.construct(*case[:-1])
        res = get_level_order(tree)
        print(res, case[-1])
