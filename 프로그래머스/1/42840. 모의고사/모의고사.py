def solution(answers):
    answer = []
    
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    
    for i, v in enumerate(answers):
        if v == person1[i % len(person1)]:
            cnt[0] += 1
        if v == person2[i % len(person2)]:
            cnt[1] += 1
        if v == person3[i % len(person3)]:
            cnt[2] += 1    

    max_cnt = max(cnt)
    for j, v in enumerate(cnt):
        if v == max_cnt:
            answer.append(j + 1)
    
    return answer