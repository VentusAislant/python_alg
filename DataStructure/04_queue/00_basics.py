"""
- 队列（Queue）作为一种先进先出（FIFO）的数据结构，是栈（LIFO）的“对偶”
- 队列：只允许在一段进行插入，在另一端进行删除的线性表
- 入队：向队列队尾插入元素。出队：删除队头元素
- Python提供了两种方便使用队列的库
"""

# 通过 queue.Queue 使用队列
from queue import Queue

def print_queue(q: Queue):
    for item in q.queue:
        print(item, end=' ')
    print()

q = Queue()
q.put(1)
q.put(2)
print_queue(q)  # 1 2
item = q.get()
print(item)
print_queue(q)  # 2


# 通过 collections.deque 使用队列 (双端队列)
from collections import deque

q  = deque([1, 2, 3])
q.append(4)
print(q)  # deque([1, 2, 3, 4])
item = q.popleft()
print(item)  # 1
print(q)  # deque([2, 3, 4])
