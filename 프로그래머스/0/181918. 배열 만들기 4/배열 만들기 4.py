def solution(arr):
    stk = []
    i = 0
    while len(arr) > i:
        if stk:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
        else:
            stk.append(arr[i])
            i += 1
            
    return stk