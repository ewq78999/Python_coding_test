# 해당 사진의 추억 점수 =사진 속 각 인물들의 그리움 점수 합
# 그리워하는 사람 이름 name, 점수를 담은 정수 배열 yearning, 사진에 찍힌 인물의 이름을 담은 photo
# photo 안의 이름 목록에서 name 안의 이름을 비교해서 찾은 후 그 아룸아 가진 yearning 값을 합침

def solution(name, yearning, photo):
    answer = []
    
    for idx1, char1 in enumerate(photo):
        score = 0
        for idx2, char2 in enumerate(name):
            if char2 in char1 :
                score += yearning[idx2]
        answer.append(score)
            
    return answer
