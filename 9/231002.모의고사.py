def solution(answers):
    answer = 0
    f_count = 0
    s_count = 0
    t_count = 0
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    l = len(answers)
    f = first[:l]
    s = second[:l]
    t = third[:l]
    
    for idx, num in enumerate(answers):
        if num == f[idx]:
            f_count += 1
        if num == s[idx]:
            s_count += 1
        if num == t[idx]:
            t_count += 1
            
        if f_count > s_count and f_count > t_count:
            answer = [1]
        elif s_count > f_count and s_count > t_count:
            answer = [2]
        elif t_count > f_count and t_count > s_count:
            answer = [3]
        elif f_count == s_count and f_count > t_count:
            answer = [1,2]
        elif f_count == t_count and f_count > s_count:
            answer = [1,3]
        elif s_count == t_count and t_count > f_count:
            answer = [2,3]
        else:
            answer = [1,2,3]
            
    return answer
    
    

def solution(answers):
    # 수포자들의 찍는 패턴
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자가 맞춘 문제의 개수
    f_count = 0
    s_count = 0
    t_count = 0
    
    # 각 수포자의 답안과 실제 답안을 비교
    for idx, num in enumerate(answers):
        # 연산자를 통해 패턴을 미리 만들지 않아도 무한히 반복하는 것처럼 구성하여 탐색 가능
        if num == first[idx % len(first)]:
            f_count += 1
        if num == second[idx % len(second)]:
            s_count += 1
        if num == third[idx % len(third)]:
            t_count += 1

    # 수포자들 간의 점수를 비교
    max_score = max(f_count, s_count, t_count)
    answer = []

    if f_count == max_score:
        answer.append(1)
    if s_count == max_score:
        answer.append(2)
    if t_count == max_score:
        answer.append(3)
            
    return answer