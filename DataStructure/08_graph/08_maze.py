"""
    走迷宫问题：
        1. BFS: 可以找到最短的路径
        2. DFS: 可以找到一条路径，不一定最短
        3. A*: 添加启发式函数指导的搜索路线，BFS均匀往各个方向探索，A*通过使用启发式函数，
               可以判断哪个方向的路线可能更快到达， 优先往终点方向探索
               使用一个估价函数 h(n) = f(n) + g(n), f(n)表示启发式代价, g(n)表示实际代价
"""
from collections import deque
import heapq


def bfs_maze(maze, start, end):
    row, col = len(maze), len(maze[0])

    visited = set()
    parent = {start: None}
    path = []
    # up, down, left right
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        cur_pos = queue.popleft()
        if cur_pos == end:
            break
        for d in direction:
            new_pos = (cur_pos[0] + d[0], cur_pos[1] + d[1])
            if 0 <= new_pos[0] < row and 0 <= new_pos[1] < col and maze[new_pos[0]][new_pos[1]] == 0:
                if new_pos not in visited:
                    queue.append(new_pos)
                    visited.add(new_pos)
                    parent[new_pos] = cur_pos

    if end not in parent:
        return []

    # restore the path
    cur_pos = end
    while cur_pos is not None:
        path.append(cur_pos)
        cur_pos = parent[cur_pos]
    path.reverse()

    return path


def dfs_maze(maze, start, end):
    row, col = len(maze), len(maze[0])
    path = []
    visited = set()
    parent = {start: None}
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def dfs_maze(pos) -> bool:
        if pos == end:
            return True
        visited.add(pos)
        for d in direction:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if 0 <= new_pos[0] < row and 0 <= new_pos[1] < col and maze[new_pos[0]][new_pos[1]] == 0:
                if new_pos not in visited:
                    parent[new_pos] = pos
                    if dfs_maze(new_pos):  # 在 new_pos 的子方向 DFS 时到达终点，可以避免剩下的方向的尝试
                        return True
        # 所有方向都走不同，没有路径
        return False

    if dfs_maze(start):
        cur_pos = end
        while cur_pos is not None:
            path.append(cur_pos)
            cur_pos = parent[cur_pos]
        path.reverse()

    return path


def a_star_maze(maze, start, end):
    row, col = len(maze), len(maze[0])

    parent = {start: None}
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def f(a, b):
        # 因为只能上下左右走，用曼哈顿距离当作, 如果可以走对角线可以用 欧几里德距离
        manhattan = abs(a[0] - b[0]) + abs(a[1] - b[1])
        # euclidean = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        return manhattan

    g_score = {start: 0}  # 记录每个节点的实际代价
    visited = set()
    heap = []
    heapq.heappush(heap, (g_score[start] + f(start, end), g_score[start], start))  # f+g, g, pos

    while heap:
        fg, g, cur_pos = heapq.heappop(heap)
        if cur_pos == end:
            break
        if cur_pos in visited:
            continue
        visited.add(cur_pos)
        for d in direction:
            new_pos = (cur_pos[0] + d[0], cur_pos[1] + d[1])
            if 0 <= new_pos[0] < row and 0 <= new_pos[1] < col and maze[new_pos[0]][new_pos[1]] == 0:
                tentative_g = g + 1  # 从当前位置移动到下一个位置的实际代价
                if new_pos not in g_score or tentative_g < g_score[new_pos]:
                    g_score[new_pos] = tentative_g
                    fg_score = tentative_g + f(new_pos, end)  # 下一个位置的启发式分数
                    heapq.heappush(heap, (fg_score, tentative_g, new_pos))
                    parent[new_pos] = cur_pos

    # 重建路径
    path = []
    cur = end
    if cur not in parent:
        return []  # 无法到达
    while cur:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


def show_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print('*', end=' ')
            else:
                print(maze[i][j], end=' ')
        print()


if __name__ == '__main__':
    # 0 can move, 1: wall
    maze = [
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    ]
    path = bfs_maze(maze, start=(0, 0), end=(9, 9))
    print(len(path))
    show_path(maze, path)

    path = dfs_maze(maze, start=(0, 0), end=(9, 9))
    print(len(path))
    show_path(maze, path)

    path = a_star_maze(maze, start=(0, 0), end=(9, 9))
    print(len(path))
    show_path(maze, path)
