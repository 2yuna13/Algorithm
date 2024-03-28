from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 물에 잠기지 않는 영역 구하기 graph[x][y] > height
def bfs(x, y, height):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 물에 잠기지 않는 영역
            if graph[nx][ny] > height and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))


# 높이별로 안전한 영역 개수 확인
# 가능한 모든 높이 -> 최소 높이 ~ 최대 높이
min_height = min(map(min, graph))
max_height = max(map(max, graph))

res = 1

for h in range(min_height, max_height + 1):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                bfs(i, j, h)
                cnt += 1

    res = max(res, cnt)

print(res)