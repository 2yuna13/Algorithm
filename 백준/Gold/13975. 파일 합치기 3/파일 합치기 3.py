import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    heapify(files)
    ans = 0
    for _ in range(k - 1):
        a = heappop(files)
        b = heappop(files)
        ans += a + b
        heappush(files, a + b)

    print(ans)