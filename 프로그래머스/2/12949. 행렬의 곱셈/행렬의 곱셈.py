# 행렬 곱셈
# arr1 행(r) * arr2 열(c)

def solution(arr1, arr2):
    r1 = len(arr1)
    r2 = len(arr2)
    c2 = len(arr2[0])
    
    answer = [[0] * c2 for _ in range(r1)]
    
    for i in range(r1): # 결과 행 인덱스
        for j in range(c2): # 결과 열 인덱스
            for k in range(r2): # 곱할 때.. 
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer