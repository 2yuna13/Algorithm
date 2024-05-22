def solution(phone_number):    
    s = len(phone_number)
    
    return '*' * (s - 4) + phone_number[s-4:]