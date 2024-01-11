l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()

def is_ok(password):
    vowels = set('aeiou')
    vowel_count = 0

    for p in password:
        if p in vowels:
            vowel_count += 1

    return vowel_count >= 1 and l - vowel_count >= 2

def dfs(level, start, path):
    if level == l:
        if is_ok(path):
            print(path)
        return

    for i in range(start, c):
        dfs(level + 1, i + 1, path + alpha[i])

dfs(0, 0, '')