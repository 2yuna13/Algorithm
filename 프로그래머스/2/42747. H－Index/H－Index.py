# 제한 사항 : 논문의 수 1,000 이하 / 인용 횟수 10,000회 이하

def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
            
    return len(citations)