from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        思想类似 二叉树的最大路径和 (124), 用递归的思路
            分别计算左右子树的直径贡献，利用一个全局变量保存最大直径
        """
        self.res = 0

        def postorder(node):
            if not node:
                return 0  # 空结点不提供直径

            # 递归左右子树的直径贡献
            left_gain = postorder(node.left)
            right_gain = postorder(node.right)

            # 当前结点作为路径中转点时的贡献
            cur_sum = left_gain + right_gain + 1

            # 更新全局最大直径
            if cur_sum > self.res:
                self.res = cur_sum

            # 返回当前结点能够提供的最大直径贡献
            return 1 + max(left_gain, right_gain)  # 只能用一边

        postorder(root)
        return self.res - 1


def construct_tree(level_order) -> TreeNode:
    """
    层序遍历序列构建二叉树：
        使用队列辅助，首先根结点入队
        每次取出一个结点，构建其左右子结点，构建完毕后左右子结点入队
    """
    queue = deque()
    root = TreeNode(level_order[0])
    queue.append(root)
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order):
            node.left = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.left)
            i += 1
        if i < len(level_order):
            node.right = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.right)
            i += 1
    return root


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1)
    ]

    solution = Solution()
    for case in cases:
        tree = construct_tree(*case[:-1])
        res = solution.diameterOfBinaryTree(tree)
        print(res, case[-1])
