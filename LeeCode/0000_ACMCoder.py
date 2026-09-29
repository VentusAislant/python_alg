import math


def solve1():
    # 单个数字输入：判断数字是否是一个平方数
    num = int(input())
    for i in range(1, int(math.sqrt(num))+1):
        if i*i == num:
            print(True)
            return
    print(False)

def solve2():
    # 一行数组输入：寻找多数元素
    nums = list(map(int, input().split()))
    candidate = None
    vote = 0
    for num in nums:
        if vote == 0:
            candidate = num

        if num == candidate:
            vote += 1
        else:
            vote -= 1
    print(candidate)

def solve3():
    # 第一行数字 n + n行数字：找最大值
    n = int(input())

    cur_max = float('-inf')
    for _ in range(n):
        x = int(input())
        if cur_max < x:
            cur_max = x

    print(cur_max)

def solve4():
    # 矩阵输入: 矩阵转置
    m, n = map(int, input().split())  # m 行 n 列
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            print(matrix[j][i], end=' ')
        print()

def solve5():
    # 字符串输入：判断回文串
    s = input()
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            print(False)
            return
    print(True)


def solve6():
    def climbStairs(n: int) -> int:
        """
        设 dp[i] 表示到 第 i 阶的走法数, 这个版本刚开始在第1阶
            dp[1]=0, dp[2]=1, dp[3]=2
        递归方程
            dp[i] = dp[i-1] + dp[i-2]
        空间优化版本，因为只依赖前两项，所以只需要两个变量
        """
        if n <= 3:
            return n-1
        a, b = 1, 2
        for i in range(4, n + 1):
            a, b = b, a + b
        return b

    # 多组测试数据：上台阶
    t = int(input())
    for _ in range(t):
        m = int(input())
        print(climbStairs(m))


def solve7():
    # 不知道测试组数（读到EOF）：计算两数之和
    import sys
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(a+b)

    # 或者
    # while True:
    #     try:
    #         a, b = map(int, input().split())
    #         print(a + b)
    #     except:
    #         break


def solve8():
    # 图的输入
    from collections import defaultdict
    graph = defaultdict(list)
    m, n = map(int, input().split())  # m 个顶点， n条边
    for _ in range(n):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    print(graph)

def solve9():
    import sys
    data = sys.stdin.read().split()  # ctrl+D 表示 EOF
    print(data)


if __name__ == '__main__':
    solve9()