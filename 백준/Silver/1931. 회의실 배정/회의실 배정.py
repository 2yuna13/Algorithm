import sys

input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))

ans = 0
now = 0
for start, end in meetings:
    if now <= start:
        now = end
        ans += 1
print(ans)