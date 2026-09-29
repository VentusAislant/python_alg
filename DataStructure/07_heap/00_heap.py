import heapq

# 将一个可迭代对象原地转化为最小堆
data = [3, 1, 4, 1, 5, 9]
heapq.heapify(data)
print(data)  # [1, 1, 4, 3, 5, 9]

# 如果每一个元素都是元组，则会默认用元组第一个元素构建最小堆
data = [(3, 'C'), (1, 'A'), (4, 'D'), (1, 'A'), (5, 'E'), (9, 'I')]
heapq.heapify(data)
print(data)  # [(1, 'A'), (1, 'A'), (4, 'D'), (3, 'C'), (5, 'E'), (9, 'I')]


# 往堆中添加一个元素，同时保持最小堆性质
data = [3, 1, 4, 1, 5, 9]
heapq.heappush(data, 10)
print(data)  # [1, 1, 4, 3, 5, 9, 10]

# 往堆中弹出一个元素，同时保持最小堆性质
item = heapq.heappop(data)
print(item)  # 1
print(data)  # [1, 3, 4, 10, 5, 9]

# 先将item加入堆，然后再弹出最小元素
item = heapq.heappushpop(data, 0)
print(item)  # 0
print(data)  # [1, 3, 4, 10, 5, 9]

# 先弹出最小元素并加入新元素
item = heapq.heapreplace(data, 0)
print(item)  # 1
print(data)  # [0, 3, 4, 10, 5, 9]

# 返回最大的 n 个元素，结果为一个降序列表
n_largest_lst = heapq.nlargest(3, data)
print(n_largest_lst)  # [10, 9, 5]

# 返回最小的 n 个元素，结果为一个升序列表
n_smallest_lst = heapq.nsmallest(3, data)
print(n_smallest_lst)  # [0, 3, 4]


# 找到数组中的第k大的值
def find_k_largest(lst, k):
    heapq.heapify(lst)
    return heapq.nlargest(k, lst)[-1]

def find_k_smallest(lst, k):
    heapq.heapify(lst)
    return heapq.nsmallest(k, lst)[-1]

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_k_largest(lst, 3))  # 8
    print(find_k_smallest(lst, 3))  # 3
