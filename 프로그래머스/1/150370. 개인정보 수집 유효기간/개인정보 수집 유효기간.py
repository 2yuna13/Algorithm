def to_days(date):
    y, m, d = map(int, date.split('.'))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    answer = []
    days = {}
    today = to_days(today) 
    
    for t in terms:
        type, m = t.split()
        days[type] = int(m) * 28

    for i, v in enumerate(privacies):
        date, type = v.split()
        
        if to_days(date) + days[type] - 1 < today:
            answer.append(i + 1)
    
    return answer