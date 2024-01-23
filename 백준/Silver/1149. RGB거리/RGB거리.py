import sys
input = sys.stdin.readline

n = int(input())
rgb_lst = []
for _ in range(n):
    rgb_lst.append(list(map(int, input().split())))

memo = [[0] * 3 for _ in range(n)]
memo[0] = rgb_lst[0]

for i in range(1, n):
    memo[i][0] = min(memo[i - 1][1], memo[i - 1][2]) + rgb_lst[i][0]
    memo[i][1] = min(memo[i - 1][0], memo[i - 1][2]) + rgb_lst[i][1]
    memo[i][2] = min(memo[i - 1][0], memo[i - 1][1]) + rgb_lst[i][2]

print(min(memo[-1]))