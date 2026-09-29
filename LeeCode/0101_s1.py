from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """
        迭代算法:
            可以用层序遍历用一个队列存储成对的结点 (t1, t2) 分别代表左右子树
            每次取出一对，判断这两个结点的值，然后将下一对插入队列
                (左子树的左结点，右子树的右结点)
                (右子树的左结点, 左子树的右结点)
        """
        if not root:
            return True

        queue = deque([(root.left, root.right)])
        while queue:
            t1, t2 = queue.popleft()

            # 都为空，继续检查下一对
            if not t1 and not t2:
                continue
            # 都不为空
            elif t1 and t2:
                if t1.val != t2.val:
                    return False
                # 按照镜像顺序加入下一层
                queue.append((t1.left, t2.right))
                queue.append((t1.right, t2.left))
            # 一个空一个不空
            else:
                return False
        return True

    def isSymmetricV1(self, root: TreeNode | None) -> bool:
        """
        递归算法:
            判断是否对称关键是需要左右子树之间的镜像关系，简单的遍历只能单独处理每个子树，无法判断这个关系
            需要判断左子树和右子数的关系：
                左子树的左 和 右子树的右 需要对应
                右子树的左 和 左子树的右 需要对应
        """
        if not root:
            return True

        def is_mirror(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True
            elif t1 and t2:
                return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
            else:
                return False

        return is_mirror(root.left, root.right)


def construct_tree(level_order):
    queue = deque()
    root = TreeNode(level_order[0])
    queue.append(root)
    i = 1
    while queue:
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


def level_order(root: TreeNode | None) -> list:
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
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
    ]
    solution = Solution()
    for input, answer in cases:
        output = solution.isSymmetric(construct_tree(input))
        print(answer, output)
