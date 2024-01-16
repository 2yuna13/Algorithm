import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color):
    visited[y][x] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[ny][nx] == 0 and board[ny][nx] == color:
                dfs(nx, ny, color)


cnt_1 = 0
cnt_2 = 0

visited = [[0] * n for _ in range(n)]

# 기본 탐색
for y in range(n):
    for x in range(n):
        if visited[y][x] == 0:
            dfs(x, y, board[y][x])
            cnt_1 += 1

visited = [[0] * n for _ in range(n)]

# 적록색약 탐색
for y in range(n):
    for x in range(n):
        if board[y][x] == 'G':
            board[y][x] = 'R'

for y in range(n):
    for x in range(n):
        if visited[y][x] == 0:
            dfs(x, y, board[y][x])
            cnt_2 += 1


print(cnt_1, cnt_2)