class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for a, b, c in flights:
            graph[a].append((b, c))

        q = []
        # 누적비용, 노드, 경유지
        heapq.heappush(q, (0, src, 0))
        visited = {}
    
        while q:
            acc, cur, stops = heapq.heappop(q)
            if cur == dst:
                return acc

            if cur not in visited or visited[cur] > stops:
                visited[cur] = stops
                for adj, cost in graph[cur]:
                    if stops <= k:
                        new_cost = acc + cost
                        heapq.heappush(q, (new_cost, adj, stops + 1))

        return -1
        