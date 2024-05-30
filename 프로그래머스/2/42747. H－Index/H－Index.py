# 논문 n ,h번 이상 인용된 논문이 h편 이상

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
        
    return len(citations)