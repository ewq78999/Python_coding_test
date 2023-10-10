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