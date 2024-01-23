import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

cnt = []
books_m = []
books_p = []

for i in books:
    if i < 0:
        books_m.append(i)
    else:
        books_p.append(i)

for i in range(0, len(books_m), m):
    cnt.append(books_m[i])

for i in range(len(books_p)-1, -1, -m):
    cnt.append(books_p[i])

cnt = [abs(i) for i in cnt]
max_cnt = max(cnt)

for i in range(len(cnt)):
    if cnt[i] == max_cnt:
        cnt[i] = cnt[i]

    else:
        cnt[i] = cnt[i] * 2

print(sum(cnt))