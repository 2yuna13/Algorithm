import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        n1 = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        n = n1 + n2 * 2

        heapq.heappush(scoville, n)
        answer += 1   
        
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1
        if scoville[0] < K and len(scoville) == 1: 
            return -1        
    
    return answer