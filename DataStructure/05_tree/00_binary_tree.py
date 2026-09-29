from collections import deque


class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def construct_from_level_order(self, level_order_lst: list | tuple):
        """
        根据层序遍历的结果构建二叉树
        :param level_order_lst: 如果当前节点为空则用符号 `#` 代替
            例如： level_order_lst = [11, 2, #, 3, 4, #, #] 表示, 最后两个 # 可以没有
                    11
                    /
                   2
                  / \
                 3  4
        :return: self
        """
        queue = deque()
        self.root = TNode(level_order_lst[0])
        queue.append(self.root)
        i = 1
        while queue and i < len(level_order_lst):
            current_parent = queue.popleft()
            # 构造左子树
            if level_order_lst[i] != '#':
                tmp_node = TNode(level_order_lst[i])
                current_parent.left = tmp_node
                queue.append(tmp_node)
            # 构造右子树
            i += 1
            if i < len(level_order_lst) and level_order_lst[i] != '#':
                tmp_node = TNode(level_order_lst[i])
                current_parent.right = tmp_node
                queue.append(tmp_node)
            i += 1
        return self

    def pre_order(self):
        """
        使用栈版本
        """
        res = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            res.append(node.data)
            # 栈是后进先出，所以需要先压入右
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def pre_order_traverse(self):
        results = []
        self._pre_order(self.root, results)
        return results

    def _pre_order(self, node, results):
        if node is not None:
            results.append(node.data)
            self._pre_order(node.left, results)
            self._pre_order(node.right, results)

    def in_order(self):
        res = []
        stack = []
        cur = self.root
        while stack or cur:
            # 一直往左走
            while cur:
                stack.append(cur)
                cur = cur.left
            # 左子树为空，此时栈顶元素为需要访问的
            cur = stack.pop()
            res.append(cur.data)
            cur = cur.right
        return res

    def in_order_traverse(self):
        results = []
        self._in_order(self.root, results)
        return results

    def _in_order(self, node, results):
        if node is not None:
            self._in_order(node.left, results)
            results.append(node.data)
            self._in_order(node.right, results)

    def post_order(self):
        """
        迭代版本
        """
        res = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            res.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        # 根 - 右 - 左 翻转后就是 左右根
        return res[::-1]

    def post_order_traverse(self):
        results = []
        self._post_order(self.root, results)
        return results

    def _post_order(self, node, results):
        if node is not None:
            self._post_order(node.left, results)
            self._post_order(node.right, results)
            results.append(node.data)

    def level_order_traverse(self):
        results = []
        queue = deque()
        queue.append(self.root)
        while queue:
            current_node = queue.popleft()
            results.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    def find(self, value):
        # 查找 value 是否在树中
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return False
        if value == node.data:
            return True
        # 是否在左右子树
        return self._find(node.left, value) or self._find(node.right, value)

    def height(self):
        # 求二叉树的高度
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def find_max(self):
        max_value = float('-inf')
        return self._find_max(self.root, max_value)

    def _find_max(self, node, cur_max):
        if node is None:
            return cur_max
        if node.data > cur_max:
            cur_max = node.data
        left_max = self._find_max(node.left, cur_max)
        right_max = self._find_max(node.right, cur_max)
        return max(left_max, right_max)

    def find_min(self):
        min_value = float('inf')
        return self._find_min(self.root, min_value)

    def _find_min(self, node, cur_min):
        if node is None:
            return cur_min
        if node.data < cur_min:
            cur_min = node.data

        left_min = self._find_min(node.left, cur_min)
        right_min = self._find_min(node.right, cur_min)
        return min(left_min, right_min)

    def pretty_print(self, node=None, prefix="", is_left=True):
        """横向打印二叉树"""
        if node is None:
            node = self.root

        # 先打印右子树
        if node.right:
            self.pretty_print(node.right, prefix + ("│   " if is_left else "    "), False)
        # 打印当前节点
        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))

        # 打印左子树
        if node.left:
            self.pretty_print(node.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.construct_from_level_order(
        [111, 22, 33, 4, 5, 6, 7, 8888, 9999, '#', '#', 1010]
    )

    bt.pretty_print()
    print(bt.pre_order())
    print(bt.pre_order_traverse())
    print(bt.in_order())
    print(bt.in_order_traverse())
    print(bt.post_order())
    print(bt.post_order_traverse())
    print(bt.level_order_traverse())
    print(bt.find(1010), bt.find(0))
    print(bt.height())
    print(bt.size())
    print(bt.find_max())
    print(bt.find_min())
