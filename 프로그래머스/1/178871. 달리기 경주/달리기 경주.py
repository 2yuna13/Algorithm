def solution(players, callings):
    position = {}
    
    for i, v in enumerate(players):
        position[v] = i
    
    for call in callings:
        current_position = position[call]
        
        front_player = players[current_position - 1]
        players[current_position], players[current_position - 1] = players[current_position - 1], players[current_position]
        
        position[call] -= 1
        position[front_player] += 1
        
    return players