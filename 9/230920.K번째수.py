def solution(array, commands):
    answer = []
    # array를 command의 i번째부터 j번째까지 자름
    # 정렬 sorted
    # k번째 숫자 return
   
    for i, j ,k in commands:
        # i:j 이때 i는 그 index 시작 위치부터, j는 j요소 직전까지만 반환
        a = array[i-1:j]
        b = sorted(a)
        answer.append(b[k-1])
    
    return answer