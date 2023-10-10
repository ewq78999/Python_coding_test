def solution(n, lost, reserve):
    answer = []
    count = 0
    
    # 오답

    for i in range(1, n+1):
        if i not in lost:  # 체육복이 있는 학생 또는 여벌이 있는 학생
            count += 1
        else:
            if i in reserve:  # 도난 당했지만 여벌이 있는 학생
                count += 1
                reserve.remove(i)  # 여벌 체육복 사용
                lost.remove(i)     # 여벌 체육복 획득
    
    # 나머지 학생들에 대해 체육복 빌려주기
    for i in reserve:
        if i-1 in lost:
            count += 1
            lost.remove(i-1)
        elif i+1 in lost:
            count += 1
            lost.remove(i+1)
            
    return count


def solution(n, lost, reserve):
    count = 0
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있고, 그 학생을 제거
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    # 체육복을 빌려줄 수 있는 경우 확인
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    # 전체 학생 수에서 체육복을 못 빌린 학생 수를 빼기
    count = n - len(set_lost)
    
    return count