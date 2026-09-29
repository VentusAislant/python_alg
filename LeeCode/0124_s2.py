from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        """
        对于图
                1
               / \
              9  20
                 / \
                15 7
        其最大路径和是 1 + 9 + 20 + 15 = 45
        因此可以递归计算左右子树的贡献，同时利用一个全局变量保存当前最大路径和
        """
        self.max_sum = float('-inf')

        def postorder(node):
            if node is None:
                return 0  # 空结点不提供最大路径和的贡献

            # 左右子树的贡献，如果是负数就不要
            left_gain = max(postorder(node.left), 0)
            right_gain = max(postorder(node.right), 0)

            # 当前结点作为最高点时的路径和 (可同时使用左右贡献)
            cur_sum = node.val + left_gain + right_gain

            # 更新全局最大路径和
            if cur_sum > self.max_sum:
                self.max_sum = cur_sum

            # 返回当前结点提供的最大路径和贡献
            return node.val + max(left_gain, right_gain)  # 只能使用一边

        postorder(root)
        return self.max_sum


def construct_tree(level_order):
    if not level_order: return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()

        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root


def level_order(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            res.append(None)
            continue

        res.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    # 去掉末尾多余的 None
    while res and res[-1] is None:
        res.pop()

    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([1, 9, 20, None, None, 15, 7], 45)
    ]
    for case in cases:
        root = construct_tree(case[0])
        print(level_order(root))
        res = solution.maxPathSum(root)
        print(res, case[-1])
