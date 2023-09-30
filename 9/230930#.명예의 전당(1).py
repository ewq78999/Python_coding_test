# k일까지는 앞의 k번째까지 중 가장 작은 숫자 출력, 이후엔 옆으로 한칸씩 이동하면서 가장 작은 수 출력 
# 최하위 점수를 삭제(min 사용)
def solution(k, score):
    answer = []
    honor = []

    for idx, num in enumerate(score):
        # idx == k-1까지 num 추가
        if idx < k:
            honor.append(num)

        # 가장 작은 수를 지우고 새로운 num 추가 
        else:
            if num >= min(honor):
                honor.remove(min(honor))
                honor.append(num)

        # 위 과정을 거친 honor에서 가장 작은 수 answer에 계속 추가  
        answer.append(min(honor))

    return answer