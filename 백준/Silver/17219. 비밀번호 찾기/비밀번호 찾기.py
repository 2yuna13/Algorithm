n, m = map(int, input().split())
password_dict = {}

for _ in range(n):
    address, password = input().split()
    password_dict[address] = password

res = []
for _ in range(m):
    target_site = input()
    res.append(password_dict[target_site])

print(*res, sep='\n')