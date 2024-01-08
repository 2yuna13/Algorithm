import sys

n = int(sys.stdin.readline())

for _ in range(n):
    input_pw = sys.stdin.readline().rstrip() 
    left = []
    right = []

    for p in input_pw:
        if p == '-':
            if left:
                left.pop()
        elif p == '<':
            if left:
                right.append(left.pop())
        elif p == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(p)

    print(''.join(left) + ''.join(reversed(right)))
