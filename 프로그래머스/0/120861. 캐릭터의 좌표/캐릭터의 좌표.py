def solution(keyinput, board):
    answer = [0, 0]
    x, y = board
    
    for i in keyinput:
        if i == "up" and answer[1] + 1 <= (y // 2) :
            answer[1] += 1
        elif i == "down" and answer[1] - 1 >= - (y // 2):
            answer[1] -= 1
        elif i == "left" and answer[0] - 1 >= - (x // 2):
            answer[0] -= 1
        elif i == "right" and answer[0] + 1 <= (x // 2):
            answer[0] += 1
            
    return answer