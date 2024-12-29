function solution(s, n) {
    var answer = '';
    const codeA = 'A'.charCodeAt();
    const codeZ = 'Z'.charCodeAt();
    const codea = 'a'.charCodeAt();
    const codez = 'z'.charCodeAt();
    
    for (let i of s) {
        let code = i.charCodeAt()
        if (codeA <= code && code <= codeZ) {
            let newCode = (code + n - codeA) % 26 + codeA;
            answer += String.fromCharCode(newCode);
        } else if (codea <= code && code <= codez){
            let newCode = (code + n - codea) % 26 + codea;
            answer += String.fromCharCode(newCode);
        } else {
            answer += ' ';
        }
    }
    return answer;
}

// 반복문 안에서 아스키코드 + n // 근데 알파벳 넘어가지 않게 숫자 빼주기