#  S: 1제곱  /   D: 2제곱   /  T: 3제곱
#  # : 지금 점수 * (-1)
#  * : 처음에도 가능, 지금과 바로 전에 나온 값을 두배로, # 에도 *2

def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        # .isnumeric() 사용해서 숫자만 뽑음
        if i.isnumeric():
            n += i
            # return n
        # 숫자가 아니면 여기로 넘어감
        elif i == 'S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            score.append(n)
            n = ''
    # return score
        
        elif i == '*':
            # 1글자보다 많을 때
            if len(score) > 1:
                # 현재 * 리스트의 두번째 마지막 요소와 마지막 요소 값 수정
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
                
        elif i == '#':
            score[-1] = score[-1] * -1
            
    return sum(score)
        
        
        