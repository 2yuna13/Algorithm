from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
visited = [False] * (n + 1)
answer = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)

def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True

    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                answer[i] = node
                q.append(i)
                visited[i] = True

bfs(graph, 1, visited)

for i in range(2, n + 1):
    print(answer[i])