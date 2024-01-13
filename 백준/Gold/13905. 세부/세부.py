from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    parent[root_x] = root_y


n, m = map(int, input().split())
s, e = map(int, input().split())

bridge = []
for _ in range(m):
    idx, adj, cost = map(int, input().split())
    bridge.append((cost, idx, adj))
bridge.sort()

parent = list(range(n + 1))
last = 0

while find(s) != find(e) and bridge:
    d, x, y = bridge.pop()
    last = d
    union(x, y)

result = last if find(s) == find(e) else 0
print(result)