def dist(point1, point2):
    y1, x1 = point1
    y2, x2 = point2
    return abs(y2 - y1) + abs(x2 - x1)

def solution(numbers, hand):
    answer = ''
    
    # 키패드 위치
    keypad = { 1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2],
    }

    # 왼손 시작 * / 오른손 시작 #
    left_loc = keypad['*']
    right_loc = keypad['#']
    
    for num in numbers:
        # 왼손 엄지손가락 사용
        if num in [1, 4, 7]:
            left_loc = keypad[num]
            answer += 'L'
        # 오른쪽 엄지손가락 사용
        elif num in [3, 6, 9]:
            right_loc = keypad[num]
            answer += 'R'
        else:
            # 두 엄지손가락의 현재 키패드 위치에서 더 가까운 엄지손가락 사용
            if dist(left_loc, keypad[num]) < dist(right_loc, keypad[num]):
                left_loc = keypad[num]
                answer += 'L'
            elif dist(left_loc, keypad[num]) > dist(right_loc, keypad[num]):
                right_loc = keypad[num]
                answer += 'R'
            # 두 엄지손가락의 거리가 같을 때
            else:
                # 왼손잡이 
                if hand == 'left':
                    left_loc = keypad[num]
                    answer += 'L'
                # 오른손잡이
                else:
                    right_loc = keypad[num]
                    answer += 'R'
    
    return answer