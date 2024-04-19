def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        target = int(i[s : s+l])
        if target > k:
            answer.append(target)
    return answer