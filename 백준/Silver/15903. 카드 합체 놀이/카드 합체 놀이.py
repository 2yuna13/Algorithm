n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

for _ in range(m):
    num = a[0] + a[1]
    a[0] = num
    a[1] = num
    a.sort()

print(sum(a))