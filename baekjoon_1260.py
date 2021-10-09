from collections import deque


# 깊이우선탐색
def dfs(start_d):
    print(start_d, end=' ')
    visited[start_d] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[start_d][i] == 1:
            dfs(i)


# 넓이우선탐색
def bfs(start_b):
    visited[start_b] = 1
    queue = deque([start_b])
    while queue:
        value = queue.popleft()
        print(value, end=' ')
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[value][i] == 1:
                queue.append(i)
                visited[i] = 1


n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for i in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)
