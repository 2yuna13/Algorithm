def solution(sizes):
    w = 0
    h = 0
    
    for size in sizes:
        w = max(w, sorted(size)[0])
        h = max(h, sorted(size)[1])
        
    return w * h