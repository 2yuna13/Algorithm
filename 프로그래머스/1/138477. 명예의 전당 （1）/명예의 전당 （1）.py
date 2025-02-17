import heapq

def solution(k, score):
    answer = []
    temp = []
    
    for num in score:
        heapq.heappush(temp, num)
        
        if len(temp) > k:
            heapq.heappop(temp)
        
        answer.append(temp[0])
        
    return answer