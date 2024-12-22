function solution(players, callings) {
    var position = {};
    for (let i = 0; i < players.length; i++) {
        position[players[i]] = i;
    }
    
    for (let call of callings) {
        let current = position[call];
        let front_player = players[current - 1];
                            
        let temp = players[current];
        players[current] = players[current - 1];
        players[current - 1] = temp;
        
        position[call]--;
        position[front_player]++;
    }
    
    return players;
}