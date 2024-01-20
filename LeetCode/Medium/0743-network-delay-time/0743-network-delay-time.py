class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        q = []
        heapq.heappush(q, (0, k))

        dist = collections.defaultdict(int)

        while q:
            acc, cur = heapq.heappop(q)

            if cur not in dist:
                dist[cur] = acc
                for adj, time in graph[cur]:
                    new_time = acc + time
                    heapq.heappush(q, (new_time, adj))

        if len(dist) == n:
            return max(dist.values())

        return -1
