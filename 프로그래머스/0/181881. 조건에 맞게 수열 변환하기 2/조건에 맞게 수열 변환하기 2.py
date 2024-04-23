def solution(arr):
    answer = 0
    
    while True:
        next_arr = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                next_arr.append(i / 2)
            elif i < 50 and i % 2 == 1:
                next_arr.append(i * 2 + 1)
            else:
                next_arr.append(i)
                
        if arr == next_arr:
            return answer
        else:
            answer += 1
            arr = next_arr
        
    return answer