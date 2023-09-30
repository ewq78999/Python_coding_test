# answer = Yes / answer = No
# 순서대로 cards1, cards2과 비교했을 때 일치하는가? 일치하면 제외하고 계속 진행할 것

def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.pop(0)
        elif cards2 and i == cards2[0]:
            cards2.pop(0)
        else:
            answer = 'No'
    
    return answer