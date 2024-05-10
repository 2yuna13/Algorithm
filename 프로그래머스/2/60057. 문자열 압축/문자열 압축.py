def solution(s):
    answer = len(s)
    
    # 압축 할 수 있는 길이(1/2)
    for i in range(1, len(s) // 2 + 1):
        comp_len = 0
        cnt = 1
        comp = ''
        
        # 압축할 길이만큼 탐색
        for j in range(0, len(s) + 1, i):
            temp = s[j : j + i]
            
            # 앞 뒤 같을 때 (압축 가능)
            if comp == temp:
                cnt += 1
            # 앞 뒤 다를 때 (압축 불가능)
            elif comp != temp:
                comp_len += len(temp)
                # 그 전에 압축한게 있다면 숫자(문자열 길이)만큼 추가
                if cnt > 1:
                    comp_len += len(str(cnt))
                    cnt = 1
                    
            comp = temp
        
        answer = min(answer, comp_len)
                
    return answer