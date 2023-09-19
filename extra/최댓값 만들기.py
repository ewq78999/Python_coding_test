def solution(numbers):
    # numbers.sort()
    # return numbers[-1] * numbers[-2]

    answer = 0
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result = numbers[i] * numbers[j]
            
            if answer < result:
                answer = result
            
    return answer
    
