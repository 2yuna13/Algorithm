m = 1000 - int(input())

lst = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in lst:
    cnt += m // coin
    m %= coin

print(cnt)

