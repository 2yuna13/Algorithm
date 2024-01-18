import sys
input = sys.stdin.readline

# 테스트 케이스 개수
t = int(input())

for _ in range(t):
    # 지원자 수
    n = int(input())
    # 서류심사 성적, 면접 성적의 순위
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort(key=lambda x: x[0])

    top = 0
    ans = 0

    for i in range(n):
        if rank[i][1] <= rank[top][1]:
            top = i
            ans += 1

    print(ans)