def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        if int(i ** 0.5) ** 2 == i:
            # 완전제곱수를 빼버린다. 16 ** 0.5 ** 4 = 16이므로 1 / 나 자신 / 나 자신 ** 5 => 3개만 약수로 존재 가능
            answer -= i
        else:
            answer += i
    
    return answer