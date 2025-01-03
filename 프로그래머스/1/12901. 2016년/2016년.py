def solution(a, b):
    dic = {0 : 'THU', 1: 'FRI', 2: 'SAT', 3: 'SUN', 4: 'MON', 5: 'TUE', 6: 'WED'}
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 일수 계산
    days = sum(month_days[:a - 1]) + b
    
    return dic[days % 7]