import sys

input = sys.stdin.readline


def find_shark():
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                space[i][j] = 0
                return i, j


def find_food(point):
    x, y = point
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    start = [point]
    time = 0
    while start:
        time += 1
        new_start = []
        can_eat = []
        for x, y in start:
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < n and 0 <= ny < n and space[nx][ny] <= shark_size and not visited[nx][ny]:
                    if 0 < space[nx][ny] < shark_size:
                        can_eat.append((nx, ny))
                    visited[nx][ny] = True
                    new_start.append([nx, ny])
        if can_eat:
            # 거리 우선 -> 가장 위 -> 가장 왼쪽 물고기 먹어야함
            can_eat.sort()
            x, y = can_eat[0]
            space[x][y] = 0
            return x, y, time
        start = new_start[:]
    return None


n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

position = find_shark()
result = 0
eat = 0
shark_size = 2
while True:
    food = find_food(position)
    if food is None:
        break
    *position, t = food
    result += t
    eat += 1
    if eat == shark_size:
        shark_size += 1
        eat = 0

print(result)