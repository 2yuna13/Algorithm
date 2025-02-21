n, m = map(int, input().split())

def dfs(start, path):
    if len(path) == m:
        print(*path)
        return

    for i in range(start, n + 1):
        dfs(i + 1, path + [i])

dfs(1, [])