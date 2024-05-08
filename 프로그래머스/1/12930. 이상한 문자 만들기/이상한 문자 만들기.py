def solution(s):
    answer = []  
    words = s.split(" ")
    
    for word in words:
        new_word = "" 
        for i, v in enumerate(word):
            if i % 2:
                new_word += v.lower()
            else:
                new_word += v.upper()
                
        answer.append(new_word)
    
    return " ".join(answer)
