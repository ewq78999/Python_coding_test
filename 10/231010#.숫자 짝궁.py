def solution(X, Y):
    answer = ''
    
    for i in X:
        if i in Y:
            answer += i
    
    A = set(answer)
    answer = sorted(A, reverse=True)
    a = ''.join(answer)
    
    if not len(a):
        a = '-1'
    
    return a