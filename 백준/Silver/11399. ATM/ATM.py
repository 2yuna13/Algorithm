import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()

ans = 0
sum_lst = []

for i in range(n):
    ans += time[i]
    sum_lst.append(ans)

print(sum(sum_lst))