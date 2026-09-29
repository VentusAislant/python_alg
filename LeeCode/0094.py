from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        递归的栈版本
        """
        if not root:
            return []
        res = []
        stack = []
        cur = root
        while stack or cur:
            # 一直往左走
            while cur:
                stack.append(cur)
                cur = cur.left

            # 左子树为空，此时栈顶元素为需要访问的
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def inorderTraversalV1(self, root: TreeNode | None) -> list[int]:
        """
        递归版本
        """
        res = []

        def inorder(node: TreeNode | None):
            # 左根右
            if node is None:
                return
            if node.left:
                inorder(node.left)
            res.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        return res


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
        if node:
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
        ([1, None, 2, 3], [1, 3, 2]),
        ([1], [1])
    ]

    solution = Solution()
    for input, answer in cases:
        tree = construct_tree(input)
        output = solution.inorderTraversal(tree)
        print(answer, output)
