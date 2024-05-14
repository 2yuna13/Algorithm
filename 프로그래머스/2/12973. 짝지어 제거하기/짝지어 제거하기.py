def solution(s):
    temp = []

    for i in s:
        if temp and temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)

    return 1 if not temp else 0