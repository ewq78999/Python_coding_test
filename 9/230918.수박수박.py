def solution(n):
    l = list('수박' * 5000)
    result = ''
    
    for idx, char in enumerate(l):
        if idx == n:
            break
        result += char
        
    return result