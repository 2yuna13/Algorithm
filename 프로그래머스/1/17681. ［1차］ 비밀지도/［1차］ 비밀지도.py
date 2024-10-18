def solution(n, arr1, arr2):
    answer = []
    
    #이진법으로 변경
    for i in range(len(arr1)):
        arr1[i] = binaryChange(arr1[i], n)
        
    for j in range(len(arr2)):
        arr2[j] = binaryChange(arr2[j], n)
    
    #두 배열 탐색하면서 # or 공백으로 표시
    for i, j in zip(arr1, arr2):
        res = ''
        for x, y in zip(i, j):
            if x == y == '0':
                res += ' '
            else:
                res += '#'      
        answer.append(res)
    
    return answer

#이진법으로 변경
def binaryChange(num, length):
    nums = []
    while num:
        num, digit = divmod(num, 2)
        nums.append(str(digit))
    return ''.join(nums)[::-1].zfill(length)