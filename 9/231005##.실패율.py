# N : 단계 수
# stages: 사람들의: 현재 단계
# result: 가장 많이 실패한 스테이지 순으로 내림차순 나열
def solution(N, stages):
    answer = []
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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