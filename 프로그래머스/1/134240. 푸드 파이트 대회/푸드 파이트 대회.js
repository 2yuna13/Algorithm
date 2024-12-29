function solution(food) {
    var answer = '';
    let arr = [];
    
    for (let i = 1; i < food.length; i++){
        let n = Math.floor(food[i]/2)
        arr.push(String(i).repeat(n));
    }
    answer = arr.join('') + '0' +  arr.reverse().join('');
    
    return answer
}