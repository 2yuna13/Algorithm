function solution(s) {
    let len = Math.floor(s.length/2);
    
    if (s.length % 2) {
        return s[len];
    } else {
        return s[len -1] + s[len];
    }
}