function solution(s) {
    var answer = '';
    
    for (let word of s.split(" ")) {
        for (let w in word) {
            if (w % 2) {
                answer += word[w].toLowerCase();
            } else {
                answer += word[w].toUpperCase();
            }
        }
        answer += " ";
    }
    
    return answer.slice(0, -1);
}