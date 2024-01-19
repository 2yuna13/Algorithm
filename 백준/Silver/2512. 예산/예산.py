import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
total_budget = int(input())

lo = 0
hi = max(lst)

ans = 0
while lo <= hi:
    total = 0
    mid = (lo + hi) // 2

    for i in lst:
        total += min(i, mid)

    if total > total_budget:
        hi = mid - 1
    else:
        ans = mid
        lo = mid + 1

print(ans)