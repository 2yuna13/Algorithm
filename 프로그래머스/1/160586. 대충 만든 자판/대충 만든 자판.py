def solution(keymap, targets):
    answer = []
    
    key_dict = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key in key_dict:
                key_dict[key] = min(key_dict[key], i + 1)
            else:
                key_dict[key] =i + 1
    
    for target in targets:
        cnt = 0
        for t in target:
            if t not in key_dict:
                answer.append(-1)
                break
            cnt += key_dict[t]

        else: answer.append(cnt)
                        
    return answer