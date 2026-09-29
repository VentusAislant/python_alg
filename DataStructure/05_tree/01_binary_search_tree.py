from collections import deque


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            # 应该到左子树
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert(node.left, data)
        else:
            # 应该到右子树
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert(node.right, data)

    def construct(self, data_lst: list | tuple):
        """
        根据固定序列构建搜二叉搜索树
        :param data_lst: 一个特定顺序的序列，元素可以比较大小
            例如： data_lst = [3, 1, 4, 2] 表示
                     3
                    / \
                   1  4
                    \
                    2
        :return: self
        """
        for data in data_lst:
            self.insert(data)
        return self

    def find(self, value):
        # 查找 value 是否在树中
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return False
        if value == node.data:
            return True
        elif value < node.data:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def delete(self, data):
        """
        实现思路：
            如果要删除的节点是叶子节点，直接删除即可
            如果要删除的节点只有一个孩子，则直接让孩子代替其即可
            如果要删除的节点有两个孩子，则需要分两种情况：
                可以用左子树中最大的值代替自己
                也可以用右子树中最小的值代替自己
        """
        self.root = self._delete(self.root, data)

    def _delete(self, node, data) -> BSTNode | None:
        # 返回 None 表示要删除这个节点，或者当前节点为空（递归边界）
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # 找到右子树最小值，替换原来的节点
                cur_node = node.right
                while cur_node.left is not None:
                    cur_node = cur_node.left

                node.data = cur_node.data  # 当前待删除节点的值替换为右子树最小值
                node.right = self._delete(node.right, cur_node.data)  # 删除右子树最小值所在节点
        return node


    def pre_order_traverse(self):
        results = []
        self._pre_order(self.root, results)
        return results

    def _pre_order(self, node, results):
        if node is not None:
            results.append(node.data)
            self._pre_order(node.left, results)
            self._pre_order(node.right, results)

    def in_order_traverse(self):
        results = []
        self._in_order(self.root, results)
        return results

    def _in_order(self, node, results):
        if node is not None:
            self._in_order(node.left, results)
            results.append(node.data)
            self._in_order(node.right, results)

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

    def pretty_print(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        if node.right:
            self.pretty_print(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))
        if node.left:
            self.pretty_print(node.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == '__main__':
    bt = BinarySearchTree()
    bt.construct([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90])

    bt.pretty_print()
    print(bt.pre_order_traverse())
    print(bt.in_order_traverse())
    print(bt.post_order_traverse())
    print(bt.level_order_traverse())
    print(bt.height())
    print(bt.size())
    print(bt.find(90), bt.find(100))
    print(bt.find_max(), bt.find_min())
    bt.delete(50)
    bt.pretty_print()
