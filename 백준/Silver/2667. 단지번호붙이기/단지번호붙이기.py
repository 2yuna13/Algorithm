n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0


def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if grid[x][y] == 1:
        cnt += 1
        grid[x][y] = 0

        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True

    return False


res = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            res.append(cnt)
            cnt = 0
res.sort()
print(len(res))
for r in res:
    print(r)