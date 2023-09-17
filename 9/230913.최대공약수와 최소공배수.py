def solution(n, m):
    # 최대공약수 계산(n,m 중 더작은 값 반환 /최대공약수 1이 되기 위해 종료값 = 0(출력되지 않음)  / 순회할 때마다 -1 씩 적용되어 줄어듬)
    #        range(start, stop, step):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            big = i
            break
    
    # 최소공배수 계산(n * m = 최대공약수 * 최소공배수)
    small = (n * m) // big
    
    return [big, small]