function solution(s) {
    var answer = '';
    let cnt = 0;
    
    for (let i of s) {
        if (i == " ") {
            answer += " ";
            cnt = 0;
            continue;
        }
        
        if (cnt % 2) {
            answer += i.toLowerCase();
            cnt ++;
        } else {
            answer += i.toUpperCase();
            cnt ++;
        }

    }
    
    return answer;
}