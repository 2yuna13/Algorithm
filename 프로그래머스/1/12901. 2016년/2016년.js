function solution(a, b) {
    var answer = '';
    let week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    let month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    
    let days = b;
    
    for (let i = 0; i < a - 1; i++) {
        days += month_days[i];
    }
    
    return week[days%7];
}