# 1부터 number까지의 기사들이 각각 가지고 있는 약수의 갯수가 limit을 넘지 않으면 다 합칩 = answer
# 만약 각각 가지고 있는 약수의 갯수가 limit을 초과하면 약수의 갯수 = power가 된 후 진행

def solution(number, limit, power):
    answer = 0

    
    for i in range(1, number+1):
        count = 0
        # 약수의 갯수를 제곱근까지만 확인하는 효율적인 방법
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                count += 1
                if j != i // j:  # j와 i/j가 다르면 i/j도 i의 약수
                    count += 1
        
        if count > limit:
            answer += power
        else:
            answer += count
        
    
    return answer