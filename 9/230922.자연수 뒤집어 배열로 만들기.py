def solution(n):
    answer = []
    # [12345]
    n = str(n)
    
    for i in n:
        #[1,2,3,4,5]
        answer.append(int(i))
        
        #[5,4,3,2,1]
    return answer[::-1]