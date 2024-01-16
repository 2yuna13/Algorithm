from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(x, y):
    q = deque([(x, y)])
    graph[y][x] = 0

    while q:
        x, y = q.popleft()

        if x == target[0] and y == target[1]:
            return graph[y][x]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[ny][nx] == 0:
                q.append([nx, ny])
                graph[ny][nx] = graph[y][x] + 1


t = int(input())
for _ in range(t):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    knight = list(map(int, input().split()))
    target = list(map(int, input().split()))
    print(bfs(knight[0], knight[1]))