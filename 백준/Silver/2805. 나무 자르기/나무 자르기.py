import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

lo = 0
hi = trees[-1]

ans = 0
# 이진 탐색
while lo <= hi:
    mid = (lo + hi) // 2 # 절단기 설정 높이
    # 잘린 나무들의 길이 계산
    cnt = 0
    for i in trees:
        if i > mid:
            cnt += i - mid


    if cnt == m:
        ans = mid
        break
    # 잘린 나무의 길이가 목표보다 작으면 절단기 설정을 줄임
    elif cnt < m:
        hi = mid - 1
    # 잘린 나무의 길이가 목표보다 크면 높이를 높임
    else:
        ans = mid
        lo = mid + 1

print(ans)