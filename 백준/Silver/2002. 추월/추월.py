n = int(input())

cnt = 0
car_dict = {}
targets = []

# 대근 (들어갈 때)
for i in range(n):
    d_cars = input()
    car_dict[d_cars] = i
# 영식 (나올 때)
for j in range(n):
    y_cars = input()
    targets.append(y_cars)

for k in range(n - 1):
    for t in range(k + 1, n):
        if car_dict[targets[k]] > car_dict[targets[t]]:
            cnt += 1
            break

print(cnt)