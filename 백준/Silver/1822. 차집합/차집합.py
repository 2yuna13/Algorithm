N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = []

for i in A:
    if i not in B:
        C.append(i)

C.sort()
print(len(C))
print(*C)