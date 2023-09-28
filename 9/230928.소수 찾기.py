def solution(n):
    count = 0
    
    for i in range(1, n+1):
        # all 함수를 사용할 때 항상 다룰 대상을 제곱근 할 것 => i가 대상이기에 int(i**0.5)+1 로 range 정함
        if i > 1 and all(i % j != 0 for j in range(2, int(i**0.5)+1)):
            count +=1
    
    return count

# 에라토스테네스의 체, 배열을 할당하고 그 안에서 참, 거짓을 반복하며 소수가 아닌 수가 걸러지게 하는 방식
# => 시간 단축 및 효율성 증가에 용이한 방식
def solution(n):
    # 1. screen이라는 이름의 리스트를 생성하고, 모든 값을 True로 초기화한다. 
    #    여기서 True는 해당 인덱스의 수가 소수임을 의미한다.
    screen = [True] * (n + 1)
    
    # 2. 0과 1은 소수가 아니므로, False로 설정한다.
    screen[0], screen[1] = False, False
    
    # 3. 2부터 n의 제곱근까지의 각 수에 대해 소수 판별을 수행한다.
    #    i가 소수일 경우, i의 배수들은 소수가 아니므로 모두 False로 설정한다.
    for i in range(2, int(n**0.5) + 1):
        if screen[i]:  # i가 소수인 경우
            for j in range(i + i, n + 1, i):  # i의 배수들을 모두 False로
                screen[j] = False
                
    # 4. 마지막으로, screen 리스트에서 True인 값의 개수를 세어 반환한다.
    #    이 값이 주어진 범위 내의 소수의 개수이다.
    return screen.count(True)