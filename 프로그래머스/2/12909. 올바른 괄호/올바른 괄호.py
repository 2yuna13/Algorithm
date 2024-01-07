def solution(s):
    answer = True
    myStack = []

    for i in range(len(s)):
        if s[i] == '(':
            myStack.append(s[i])
        else:
            if len(myStack) == 0:
                answer = False
                break
            else:
                myStack.pop()

    if len(myStack) != 0:
        answer = False

    return answer