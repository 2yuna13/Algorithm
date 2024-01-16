from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * l for _ in range(l)]
    visited[y][x] = 1

    while q:
        x, y = q.popleft()

        if x == target[0] and y == target[1]:
            return visited[y][x] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[ny][nx] == 0:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1


t = int(input())
for _ in range(t):
    l = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    print(bfs(start[0], start[1]))