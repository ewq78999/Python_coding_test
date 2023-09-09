def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        a = str(bin(i|j)[2:])
        a = a.rjust(n, '0')
        b = a.replace('1', '#').replace('0', ' ')
        answer.append(b)
    
    return answer

# zip으로 짝지어줌

# bin으로 이진수로 바꿔준 후 string 사용해 글자로 변환시킴. 문자열 앞에 '0b' 가 붙기에
# [2:]를 사용해 앞글자 2개 잘라줌
# oct()를 사용하면 8진수로 바꿔주고 문자열 앞에 'Oo'가 붙음
# hex()를 사용하면 16진수로 바꿔주고 문자열 앞에 'Ox'가 붙음

# rjust를 통해 만약 a가 n보다 짧다면 그만큼 왼쪽에 '0'을 채워주며 재정의해줌

# replace를 통해 1을 #로, 0을 _로 바꿔주고 append(b)로 answer에 b값을 넣어주고 return

######### 추가 공부를 원할 경우, kakao blind test & 구현 & 문자열 문제 등을 공부할 것