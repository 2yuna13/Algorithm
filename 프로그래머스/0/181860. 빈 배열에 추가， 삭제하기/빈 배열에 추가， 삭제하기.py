def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)):
         # flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가
        if flag[i] == True:
            answer.extend([arr[i]] * (arr[i] * 2))
        # flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거
        else:
            answer = answer[:-arr[i]]
            
    return answer