function solution(a, b, n) {
    var answer = 0;
    
    // 콜라 병 교환 a => b, 가지고 있는 빈병 n
    while (n >= a) {
        let r = Math.floor(n / a) * b
        answer += r
        n = r + n % a
    }
    
    return answer;
}