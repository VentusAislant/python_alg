from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        """
        遍历过程中不断计算当前路径和以及总和即可, 只有到叶子结点才需要将 cur_sum 添加到 total_sum 中
        """

        def preorder(node, cur_sum=0):
            cur_sum = cur_sum * 10 + node.val
            if node.left is None and node.right is None:
                return cur_sum  # 叶子结点直接返回当前路径和即可

            left_sum, right_sum = 0, 0
            if node.left:
                left_sum = preorder(node.left, cur_sum)

            if node.right:
                right_sum = preorder(node.right, cur_sum)

            return left_sum + right_sum

        return preorder(root)


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
        ([1, 2, 3], 25),
        ([4, 9, 0, 5, 1], 1026)
    ]
    for case in cases:
        root = construct_tree(case[0])
        print(level_order(root))
        res = solution.sumNumbers(root)
        print(res, case[-1])
