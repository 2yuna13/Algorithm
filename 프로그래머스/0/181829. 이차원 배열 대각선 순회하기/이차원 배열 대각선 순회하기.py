def solution(board, k):
    answer = 0
    
    for i, v in enumerate(board):
        for j in range(len(v)):
            if i + j <= k:
                answer += board[i][j]
    
    return answer