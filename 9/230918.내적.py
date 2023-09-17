def solution(a, b):
    result = 0
    
    for idx, num in enumerate(a):
        result += num * b[idx]
        
    return result

# def solution(a, b):
#     l = len(a)
#     result = 0
    
#     for i in range(l):
#         result += a[i] * b[i] 
    
#     return result


# def solution(a, b):

#     return sum([x*y for x, y in zip(a,b)])