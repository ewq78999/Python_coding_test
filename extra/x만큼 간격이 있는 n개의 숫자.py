def solution(x, n):
    answer = []
    
    # x를 n번 만큼 각각 더해줘야함
    for i in range(1, n+1):
        answer.append(x*i)
       
    return answer


# def solution(x, n):
#     answer = []
#     i = 1
    
#     while i <= n:
#         answer.append(x*i)
#         i += 1
       
#     return answer