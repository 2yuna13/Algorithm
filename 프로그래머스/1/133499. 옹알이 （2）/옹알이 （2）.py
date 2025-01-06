def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        last_babble = ''
        valid = True
        
        while word:
            found = False
            for babble in lst:
                if word.startswith(babble):
                    if last_babble == babble:
                        valid = False
                        break
                
                    last_babble = babble
                    word = word[len(babble):]
                    found = True
                    break

            if not found:
                valid = False
                break

        if valid and not word:
            answer += 1
            
    return answer
