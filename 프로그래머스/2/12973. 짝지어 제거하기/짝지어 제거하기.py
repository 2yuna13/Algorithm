def solution(s):
    temp = []

    for i, v in enumerate(s):
        if temp and temp[-1] == v:
            temp.pop()
        else:
            temp.append(v)

    return 1 if not temp else 0