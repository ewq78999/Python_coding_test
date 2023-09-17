def solution(d, budget):
    # 일단 오름차순으로 정렬
    d.sort()
    result = 0
    
    # 쓰고 보니 index가 필요없다, 그냥 'for money in d' 로 사용해도 됐을 듯
    for index, money in enumerate(d):
        if budget >= money:  # 예산이 신청 금액보다 크거나 같다면
            result += 1  # 결과에 한 번 추가
            budget -= money  # 예산 - 신청 금액
        else:
            break  # 예산이 부족하면 종료

    return result
    
