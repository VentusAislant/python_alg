from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list:
        """
        层序遍历，每层累加计算平均值即可
        """
        if root is None:
            return []

        queue = deque([root])
        res = []
        while queue:
            cur_layer_size = len(queue)
            cur_sum = 0
            for i in range(cur_layer_size):
                node = queue.popleft()
                cur_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_sum / cur_layer_size)
        return res


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
        ([3, 9, 20, None, None, 15, 7], [3.00000, 14.50000, 11.00000]),
    ]
    for case in cases:
        tree = construct_tree(case[0])
        res = solution.averageOfLevels(tree)
        print(res, case[-1])
