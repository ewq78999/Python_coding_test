#     # 오답
#     answer = ''
#     Y = list(Y)
    
#     for i in X:
#         if i in Y:
#             answer += i
#             Y.remove(i)
            
#     answer = ''.join(sorted(answer, reverse=True))
    
#     # {}를 사용해 집합 표현, '0'만을 포함하는 집합인지 확인
#     if set(answer) == {'0'}:
#         answer = '0'
    
#     if len(answer) == 0:
#         answer = '-1'
    
#     return answer

def solution(X, Y):
    answer = []
    # 중복값을 없앤 것들의 교집합
    for i in (set(X) & set(Y)):
        # 같은 수가 count(i) -1 까지 반복되서 추가되게
        # 그러니까 만약 5가 X에 3개 있어도 Y에 2개만 있기에 min(2)만큼만 추가되게 함
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)
            
    answer.sort(reverse=True)
    
    if set(answer) == {'0'}:
        answer = '0'
    
    if len(answer) == 0:
        answer = '-1'
        
    return ''.join(answer)