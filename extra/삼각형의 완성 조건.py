def solution(sides):
    s = sorted(sides)
    l = len(s)
    
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(i+2, l):
                if s[i] + s[j] > s[k]:
                    answer = 1
                else: answer = 2
                    
    return answer
    
    
#     sides.sort()
#     answer = 0
    
#     if sides[0] + sides[1] > sides[2]:
#         answer = 1
#     else:
#         answer = 2
        
#     return answer
    
    
    