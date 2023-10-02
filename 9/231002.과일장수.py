# k점이 최상품의 사과, 1점이 최하품의 사과
# 남은 사과가 m보다 적으면 멈춤 => len(score) < m 이면 break
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    # range('시작값', '종료값', '중분(묶는 범위)')
    for i in range(0, len(score), m):
        box = score[i:i+m]
        
        if len(box) == m:
            answer += min(box) * m      
    
    return answer