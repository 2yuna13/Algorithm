def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    answer = ''.join(numbers)
    
    if '0' * len(numbers) == answer:
        return '0'
    
    return answer
    