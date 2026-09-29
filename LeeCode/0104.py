from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        广度优先遍历思想：最大深度等于层数，每次遍历一层
        """
        if not root:
            return 0

        max_depth = 0
        queue = deque()
        queue.append(root)
        while queue:
            # 每次处理完当前层所有结点
            cur_layer_size = len(queue)
            for _ in range(cur_layer_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_depth += 1

        return max_depth

    def maxDepthV1(self, root: TreeNode | None) -> int:
        """
        深度优先遍历思想
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


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
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2)
    ]

    solution = Solution()
    for input, answer in cases:
        tree = construct_tree(input)
        output = solution.maxDepth(tree)
        print(answer, output)
