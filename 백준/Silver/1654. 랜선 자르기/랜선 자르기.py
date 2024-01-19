import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

lo = 1
hi = max(lst)

ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    for i in lst:
        cnt += i // mid

    if cnt < n:
        hi = mid - 1
    else:
        ans = mid
        lo = mid + 1

print(ans)