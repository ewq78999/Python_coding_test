def solution(n):
    answer = 0
    pizza = 7
    
    if n % pizza == 0:
        answer = n // 7
    else:
        answer = n // 7 + 1

    
    
    return answer