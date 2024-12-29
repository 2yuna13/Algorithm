function solution(food) {
    var answer = '';
    let temp = '';
    
    for (let i = 1; i < food.length; i++){
        let n = Math.floor(food[i] / 2);
        if (n > 0) {
            let repeatedIndex = String(i).repeat(n);
            temp += repeatedIndex;
            answer = repeatedIndex + answer;
        }
    }
    
    return temp + '0' + answer;
}