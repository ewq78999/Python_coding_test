def solution(babbling):
    answer = 0
    talk = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        for j in talk:
        
            if j * 2 not in i:
                i = i.replace(j,' ')
                
        # i 오른쪽에 공백이 없을 때, 즉 모두 공백일 때 
        if not i.rstrip():
            answer += 1
            
    return answer