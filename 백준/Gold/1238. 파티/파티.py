import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    q = []
    dist = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        acc, cur = heapq.heappop(q)
        if dist[cur] < acc:
            continue

        for i in graph[cur]:
            dst = i[0]
            cost = acc + i[1]

            if cost < dist[dst]:
                heapq.heappush(q, (cost, dst))
                dist[dst] = cost

    return dist[end]


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

t = 0
for i in range(1, n + 1):
    if i == x:
        continue
    t = max(t, dijkstra(i, x) + dijkstra(x, i))

print(t)