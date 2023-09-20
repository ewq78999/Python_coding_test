def solution(t, p):
    answer = 0
    l = len(t)
    # t에서 p와 길이가 같은 부분문자열 추출 필요
    # 만약 남은 t의 길이가 p의 길이보다 짧다면 추출할 수 없으므로 len(p)를 뺴고 range니까 종료 인덱스 +1
    for i in range(l - len(p) + 1):
        # 현재 글자 "" 상태니까 숫자 비교하려면 int() 사용해야 함
        a = int(t[i:i+len(p)])
        if a <= int(p):
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
                