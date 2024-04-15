str = input()
answer = []
for s in str:
    if s.isupper() == True:
        s = s.lower()
        answer.append(s)
    else:
        s = s.upper()
        answer.append(s)

print(''.join(answer))

