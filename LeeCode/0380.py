import random


class RandomizedSet:

    def __init__(self):
        """
        使用字典 + 列表：
            字典存储 val 到 id 的映射
            列表存储 val

            字典的 in 操作时间复杂度为 O(1)，但是随机取数需要转化成列表
        """
        self.val2id = dict()
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.val2id:
            return False
        else:
            self.elements.append(val)
            self.val2id[val] = len(self.elements) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.val2id:
            return False
        else:
            # 为了避免 elements 随着使用过程不断出现空缺的地方，需要将待删除元素移动到尾部再删除
            idx = self.val2id[val]
            last_val = self.elements[-1]
            self.elements[idx] = last_val
            self.val2id[last_val] = idx  # 别忘记更新最后一个元素的新位置
            self.elements.pop(-1)
            del self.val2id[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


if __name__ == '__main__':
    rs = RandomizedSet()
    a = rs.insert(1)  # 向集合中插入 1 。返回 true 表示 1 被成功地插入。
    print(a, True)
    a = rs.remove(2)  # 返回 false ，表示集合中不存在 2 。
    print(a, False)
    a = rs.insert(2)  # 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
    print(a, True)
    a = rs.getRandom()  # getRandom 应随机返回 1 或 2
    print(a, "1或2")
    a = rs.remove(1)  # 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
    print(a, True)
    a = rs.insert(2)  # 2 已在集合中，所以返回 false 。
    print(a, False)
    a = rs.getRandom()  # 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
    print(a, 2)
