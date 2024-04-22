def solution(my_string):
    answer = [0] * 26 * 2
    for str in my_string:
        if (ord(str) - 65) < 26:
            answer[ord(str) - 65] += 1
        else:
            answer[ord(str) - 71] += 1
    return answer