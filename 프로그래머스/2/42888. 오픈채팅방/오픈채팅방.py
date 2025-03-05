def solution(record):
    answer = []
    user_dict = {}
    actions = []
    
    for i in record:
        action = i.split()
        if action[0] == 'Enter':
            user_dict[action[1]] = action[2]
            actions.append((action[0], action[1]))
        elif action[0] == 'Leave':
            actions.append((action[0], action[1]))
        elif action[0] == 'Change':
            user_dict[action[1]] = action[2]
            
    for action, user_id in actions:
        if action == 'Enter':
            answer.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        elif action == 'Leave':
            answer.append(f"{user_dict[user_id]}님이 나갔습니다.")
    
    return answer