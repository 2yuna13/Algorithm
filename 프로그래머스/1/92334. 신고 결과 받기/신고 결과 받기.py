def solution(id_list, report, k):
    answer = []
    
    # 동일한 유저에 대한 신고 1회로 처리
    report = set(report)
    
    # 신고당한 사람별 신고자 리스트
    reported = {}
    for i in report:
        a, r = i.split()
        if r not in reported:
            reported[r] = []
        reported[r].append(a)
    
    # 메일 받을 횟수 저장
    cnt = {user: 0 for user in id_list}
    
    # k 이상일 경우 신고자들에게 메일 전송
    for r, a in reported.items():
        if len(a) >= k:
            for j in a:
                cnt[j] += 1
        
    return [cnt[user] for user in id_list]