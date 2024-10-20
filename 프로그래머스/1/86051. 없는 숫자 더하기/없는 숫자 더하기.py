def solution(numbers):
    lst = [i for i in range(10)]
    for num in numbers:
        lst.remove(num)

    return sum(lst)