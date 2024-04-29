def solution(array):
    freq = {}
    
    for i in array:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    
    sorted_freq = sorted(freq.items(), key = lambda x: x[1],reverse = True)
    
    if len(sorted_freq) > 1 and sorted_freq[0][1] == sorted_freq[1][1]:
        return -1        
        
    return sorted_freq[0][0]