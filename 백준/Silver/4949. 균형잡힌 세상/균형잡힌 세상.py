def is_balanced(s):
    opener = '(['
    close = ')]'
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        elif char in close:
            if not stack:
                return False
            top = stack.pop()
            if opener[close.index(char)] != top:
                return False

    return not stack


while True:
    sentence = input()
    if sentence == '.':
        break
    res = is_balanced(sentence)
    if res:
        print('yes')
    else:
        print('no')