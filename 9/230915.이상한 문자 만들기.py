def solution(s):
    answer = ''
    
    # 각 단어는 하나 이상의 공백문자로 구분
    word_list = s.split(' ')
    print(word_list)
    
    for i in word_list:
        for index, char in enumerate(i):
            # index 짝수면 대문자로
            if index % 2 == 0:
                answer += char.upper()
            # 아니면(홀수면) 
            else:
                answer += char.lower()
        # for 한 번 진행되고 ' ' 추가
        answer += ' '

    # 뒤 공백 잘라서 답 제출
    return answer[:-1]







    