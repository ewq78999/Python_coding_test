def solution(n):
    # 문자열로 설정
    a = ''
    while n:
    # n을 3으로 나눈 몫, r = n을 3으로 나눈 후 나머지 값
        n, r = divmod(n, 3)
    # 문자열에 문자(r = n을 3으로 나눈 후 나머지 값) 추가, 이 과정을 통해 a에는 n의 3진법 표현이 뒤집어져서 저장
        a += str(r)
        
    # 뒤집어진 3진법 숫자를 10진법으로 변환 => (십진법 변환)int(a, 3(3진법인거 알려줌))
    return int(a, 3)


# def solution(n):
#     a = ''
#     while n:
#         a += str(n % 3)
    # n을 3으로 나눈 몫을 새로운 n의 값으로 업데이트하여 while문이 다음 자리의 n을 계산할 수 있게 반복시킴
#         n = n // 3

#     answer = int(a, 3)
#     return answer