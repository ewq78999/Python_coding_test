# 콜라를 받기 위해 줘야하는 병수 a, 빈 병 a개를 가져다주면 마트가 주는 콜라 병 수 b, 현재 가지고 있는 빈병의 개수 n
def solution(a, b, n):
    answer = 0
    
    while n >= a:
        n -= a
        answer += b
        n += b
    

    return answer
