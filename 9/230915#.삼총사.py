def solution(number):
    result = 0
    # number 길이
    n = len(number)
    
    # i__ => '마지막 위치 - 2' 까지 가능
    for i in range(n - 2):
        # ij_ => i+1 위치면서 '마지막 위치 - 1' 까지 가능
        for j in range(i + 1, n - 1):
            # ijk => j+1 위치면서 '마지막 위치' 까지 가능
            for k in range(j + 1, n):
                # i,j,k 위치의 number[] 안의 숫자 합 == 0 이면
                if number[i] + number[j] + number[k] == 0:
                    result += 1
    return result
            
            







    