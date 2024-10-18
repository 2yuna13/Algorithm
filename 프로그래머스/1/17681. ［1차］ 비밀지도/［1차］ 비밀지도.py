def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        # bin 이용해서 이진수 변환, 비트 OR 연산
        bin_or = bin(arr1[i] | arr2[i])[2:]
        # 길이를 n만큼 채워줌
        bin_or = bin_or.zfill(n)
        
        res = bin_or.replace('1', '#').replace('0', ' ')
        answer.append(res)
    
    return answer
