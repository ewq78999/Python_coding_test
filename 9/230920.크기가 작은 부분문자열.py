def solution(t, p):
    answer = 0
    P = int(p)
    T = len(t)
    
    for i in range(T - len(p) + 1):
        a = int(t[i:i+len(p)])
        if a <= P:
            answer += 1
            
    return answer
  
    
# def solution(t, p):
#     answer = 0
#     P = int(p)
    
#     for idx, char in enumerate(t):
#         a = t[idx:idx+len(p)]
        
#         if len(a) == len(p):
#             if int(a) <= P:
#                 answer += 1
#     return answer