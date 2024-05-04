def solution(numer1, denom1, numer2, denom2):
    
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    divisor = []
    
    for i in range(1, numer + 1):
        if numer % i == 0:
            for j in range(1, denom + 1):
                if denom % j == 0 and i == j:
                    divisor.append(i)

    n = divisor[-1]
    
    if n != 0:
        numer //= n
        denom //= n

    return [numer, denom]