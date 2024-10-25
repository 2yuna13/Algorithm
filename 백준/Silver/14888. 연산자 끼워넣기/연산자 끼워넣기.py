n = int(input())
#숫자
num = list(map(int, input().split()))
#연산자
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

def dfs(i, now):
    global max_value, min_value, add, sub, mul, div

    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / num[i]))
            div += 1


dfs(1, num[0])

print(max_value)
print(min_value)