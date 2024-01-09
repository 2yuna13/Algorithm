n = int(input())
a = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

res = []
for num in targets:
    if num in a:
        res.append(1)
    else:
        res.append(0)
        
print(*res, sep='\n')