def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        #바구니로 옮기고 캐릭터 위치 -> 0
        for j in board:
            if j[i - 1] != 0:
                basket.append(j[i - 1])
                j[i - 1] = 0
                break
        # 바구니에 쌓고 직전 캐릭터와 동일하면 pop, answer += 2
        if len(basket) > 1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
    
    return answer