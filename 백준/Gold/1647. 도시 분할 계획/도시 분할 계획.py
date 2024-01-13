from sys import stdin
input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    parent[root_x] = root_y

n, m = map(int, input().split())
edges = []
for _ in range(m):
    idx, adj, cost = map(int, input().split())
    edges.append((cost, idx, adj))
edges.sort()

parent = list(range(n + 1))
result = 0
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
    cost, x, y = edge
    if find(x) != find(y):
        union(x, y)
        result += cost
        last = cost

print(result - last)