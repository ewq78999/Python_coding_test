def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = lottos.count(0)
    
    # 4개 번호가 일치하면 3등, 2개 번호가 일치하면 5등 
    # 0은 어떤 수로도 변할수도 없고, 아니라고 가정할 때는 그냥 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                count += 1
                
    if count + zero_count == 6:
        answer.append(1)
    if count + zero_count == 5:
        answer.append(2)
    if count + zero_count == 4:
        answer.append(3)
    if count + zero_count == 3:
        answer.append(4)
    if count + zero_count == 2:
        answer.append(5)
    if count + zero_count == 1 or count + zero_count == 0:
        answer.append(6)
        
    if count == 6:
        answer.append(1)
    if count == 5:
        answer.append(2)
    if count == 4:
        answer.append(3)
    if count == 3:
        answer.append(4)
    if count == 2:
        answer.append(5)
    if count == 1 or count == 0:
        answer.append(6)
    

    return answer