from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
lessons = [list(map(int, input().split())) for _ in range(n)]
lessons.sort()

heap = []
heappush(heap, lessons[0][1])

for i in range(1, n):
    if lessons[i][0] >= heap[0]:
        heappop(heap)
    heappush(heap, lessons[i][1])

print(len(heap))