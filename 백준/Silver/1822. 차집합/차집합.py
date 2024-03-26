N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = []

for i in A:
    if i not in B:
        C.append(i)

print(len(C))
print(*sorted(C))