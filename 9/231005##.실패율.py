def solution(N, stages):
    # 딕셔너리 생성
    fail_per = {}
    answer = 0
    people = len(stages)
    
    for i in range(1, N+1):
        # count를 통해 i의 갯수(빈도)를 반환, ex) 1은 1개 있으므로 1 반환, 2는 3개 있으므로 3 반환
        fail = stages.count(i)
        # 다 떨어지고 도달한 유저가 없으면
        if people == 0:
            # 실패율을 0으로 정의
            fail_per[i] = 0
        else:
            # i : fail/people 로 키 : 값을 할당
            fail_per[i] = fail / people
            people -= fail
            
    # .get으로 반환된 fail_per값을 key로 해서 sorted한다, 이후 내림차순
    answer = sorted(fail_per, key=fail_per.get, reverse=True)
    
    return answer
    
    

    
#     level = []
#     fail1 = 0
#     fail2 = 0
#     fail3 = 0
#     fail4 = 0
#     fail5 = 0
#     fail1_per = 0
#     fail2_per = 0
#     fail3_per = 0
#     fail4_per = 0
#     fail5_per = 0
    
#     # 8명, 5명 시작
#     people = len(stages)

#     for i in range(1, N+1):
#         level.append(i)
        
#     for j in stages:
#         if j <= level[0]:
#             fail1 += 1
#             fail1_per = fail1 / people
#             people = people - fail1
            
#         elif j <= level[1] and j >= level[0]:
#             fail2 += 1
#             fail2_per = fail2 / people
#             people = people - fail2
            
#         elif j <= level[2] and j >= level[1]:
#             fail3 += 1
#             fail3_per = fail3 / people
#             people = people - fail3
            
#         elif j <= level[3] and j >= level[2]:
#             fail4 += 1
#             fail4_per = fail4 / people
#             people = people - fail4
            
#         elif j <= level[4] and j >= level[3]:
#             fail5 += 1
#             fail5_per = fail5 / people
#             people = people - fail5
            
#         else:
#             fail5_per = 0
    

#     return fail3_per