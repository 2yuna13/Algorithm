def solution(code):
    answer = ''
    mode = 0
    idx = 0
    
    while idx < len(code):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            else:
                if idx % 2 == 0:
                    answer += code[idx]
        else:
            if code[idx] == "1":
                mode = 0
            else:
                if idx % 2:
                    answer += code[idx]
        idx += 1
    
    return "EMPTY" if answer == "" else answer