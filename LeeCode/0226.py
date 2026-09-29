from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        遍历一遍，将每个结点的左右结点翻转即可
        """
        if not root:
            return None

        # 先翻转子树还是当前结点都一样
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


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


def level_order(root: TreeNode):
    """
    获取层序遍历序列
        使用辅助队列，每遍历一个结点，将其放入队列即可
    """
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == '__main__':
    cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1])
    ]

    solution = Solution()
    for input, answer in cases:
        tree = construct_tree(input)
        output = solution.invertTree(tree)
        print(answer, level_order(output))
