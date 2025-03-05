def solution(record):
    answer = []
    user_dict = {}
    
    for i in record:
        action = i.split()
        
        if action[0] == 'Enter' or action[0] == 'Change':
            user_dict[action[1]] = action[2]
            
    for j in record:
        action = j.split()
        nickname = user_dict[action[1]]
        
        if action[0] == 'Enter':
            answer.append(f"{nickname}님이 들어왔습니다.")
        elif action[0] == 'Leave':
            answer.append(f"{nickname}님이 나갔습니다.")
    
    return answer