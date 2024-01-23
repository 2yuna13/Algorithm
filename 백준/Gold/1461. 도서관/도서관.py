import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

left = []
right = []
for book in books:
    if book < 0:
        left.append(book)
    else:
        right.append(book)

cnt = []
left.sort()
right.sort()

for i in range(0, len(left), m):
    cnt.append(abs(left[i]))

for i in range(len(right)-1, -1, -m):
    cnt.append(abs(right[i]))

cnt.sort()
total_cnt = sum(cnt) * 2 - cnt[-1]

print(total_cnt)