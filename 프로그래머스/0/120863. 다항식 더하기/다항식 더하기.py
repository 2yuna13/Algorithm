def solution(polynomial):
    polynomial = polynomial.split(" + ")
    
    x = 0
    num = 0
    
    for i in polynomial:
        if i.isdigit():
            num += int(i)
        elif i == "x":
            x += 1
        elif "x" in i:
            x += int(i[:-1])
            
    if x == 0:
        return f"{num}"
    elif x == 1:
        if num > 0:
            return f"x + {num}"
        else:
            return "x"
    else:
        if num > 0:
            return f"{x}x + {num}"
        else:
            return f"{x}x"
            