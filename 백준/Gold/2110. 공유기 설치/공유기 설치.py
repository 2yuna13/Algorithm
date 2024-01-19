import sys
input = sys.stdin.readline

def install_router(lst, c):
    # 이분 탐색을 위한 정렬
    lst.sort()

    # 이분 탐색 대상은 '최대 거리' / 최솟값은 1, 최댓값은 양 끝값의 차이.
    lo = 1
    hi = lst[-1] - lst[0]
    min_gap = 0

    # 최대 거리를 찾을 때까지 이분 탐색
    while lo <= hi:
        mid = (hi + lo) // 2
        # 0번째 요소에 항상 설치하므로 1개로 초기화
        cnt = 1
        cur = lst[0]
        # 1번째 ~ 마지막 요소를 연결
        for i in range(1, len(lst)):
            # 연결만 된다면 더 멀리 있는 것도 괜찮음
            if lst[i] >= cur + mid:
                cur = lst[i]
                cnt += 1

        if cnt >= c:
            min_gap = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return min_gap


n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
print(install_router(lst, c))