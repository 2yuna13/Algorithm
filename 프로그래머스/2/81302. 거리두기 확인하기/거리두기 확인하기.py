# 응시자는 거리두기를 위해 가까이에 앉으려면 파티션을 사이에 두고 있어야 한다.
# 거리는 |r1 - r2| + |c1 - c2| > 2
# P 응시자 O 빈테이블 X 파티션 / 대기실 5x5
# 거리두기 지키면 1 안지키면 0
# 오른쪽 y+1 / 아래 x+1 / 대각선왼 y+1 x+1 / 대각선오 y-1 x+1 
# 오른쪽 0 그 오른쪽 / 아래 0 그 아래

def check_distance(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == 'P':
                # 오른쪽, 아래 확인
                for dx, dy in [(0, 1), (1, 0)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'P':
                        return 0  

                # 대각선 좌우 확인
                for dx, dy in [(1, 1), (1, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'P':
                        if place[x][ny] != 'X' or place[nx][y] != 'X':
                            return 0
                        
                # 2칸 떨어진 경우 확인
                for dx, dy in [(0, 2), (2, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'P':
                        # 파티션 확인
                        if dy == 2: 
                            if place[x][y + 1] != 'X':
                                return 0 
                        elif dx == 2:
                            if place[x + 1][y] != 'X':
                                return 0       
                            
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(check_distance(place))
        
    return answer