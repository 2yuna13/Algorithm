n = int(input())

lst = []

for _ in range(n):
    lst.append(input().split())

lst.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for l in lst:
    print(l[0])