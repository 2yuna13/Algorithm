def solution(num_list):
    answer = 1
    
    for num in num_list:
        answer *= num
    
    return 0 if answer > sum(num_list) ** 2 else 1