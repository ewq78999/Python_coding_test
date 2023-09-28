# 벽의 구역 길이: n
# 롤러의 길이: m
# 다시 칠하기로 한 구역: section
# 이때 n에 있는 section을 최소한으로 m으로 페인트칠을 하는 count를 세라
# m 길이의 롤러로 칠할 때 n을 벗어나지 않아야 한다.
def solution(n, m, section):
    count = 0
    end = 0
    
    for i in section:
        if i > end and n >= end:
            # end에 현재 위치 i + roller 길이 할당
            end = i + m - 1
            count += 1
            
    return count