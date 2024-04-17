def solution(a, b, c, d):    
    # 네 주사위가 p로 같으면
    if a == b == c == d:
        return 1111 * a
    
    # 세 주사위가 p로 같고, 나머지 하나가 q 
    elif a == b == c:
        return (10 * a + d) ** 2
    elif a == b == d:
        return (10 * a + c) ** 2
    elif a == c == d:
        return (10 * a + b) ** 2
    elif b == c == d:
        return (10 * b + a) ** 2
    
    # 두 개씩 같은 값, 각 p, q로 하면
    elif a == b and c == d:
        return (a + c) * abs(a - c)
    elif a == c and b == d:
        return (a + b) * abs(a - b)
    elif a == d and b == c:
        return (a + c) * abs(a - c)
    
    # 두 주사위가 p로 같고, 나머지 각 q, r이라 하면
    elif a == b:
        return c * d
    elif a == c:
        return b * d
    elif a == d:
        return b * c
    elif b == c:
        return a * d
    elif b == d:
        return a * c
    elif d == c:
        return a * b

    # 모두 다르면
    else:
        return min(a, b, c, d)
