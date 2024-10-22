def solution(players, callings):
    position = {player : i for i, player in enumerate(players)}
    
    for c in callings:
        current_position = position[c]
        
        #딕셔너리 값 변경
        position[c] -= 1
        position[players[current_position - 1]] += 1
        
        #실제 값 변경
        players[current_position], players[current_position - 1] = players[current_position - 1], players[current_position]
        
    return players