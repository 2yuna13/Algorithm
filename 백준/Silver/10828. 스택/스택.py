import sys

def push(stack, x):
    stack.append(x)
    
def pop(stack):
    if len(stack) > 0:
        a = stack[-1]
        stack.pop()
        return a        
    else:
        return -1
    
def size(stack):
    return len(stack)
    
def empty(stack):
    if size(stack) == 0:
        return 1
    else:
        return 0
    
def top(stack):
    if len(stack) > 0:
        return stack[-1]
    else:
        return -1

n = int(sys.stdin.readline())

my_stack = []

for _ in range(n): 
    user_input = sys.stdin.readline().split()
    
    if user_input[0] == "push":
            num = int(user_input[1])
            push(my_stack, num)

    elif user_input[0] == "pop":
            print(pop(my_stack))
            
    elif user_input[0] == "size":
            print(size(my_stack))
            
    elif user_input[0] == "empty":
            print(empty(my_stack))
            
    elif user_input[0] == "top":
            print(top(my_stack))