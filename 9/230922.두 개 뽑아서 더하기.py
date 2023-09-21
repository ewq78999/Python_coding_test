def solution(numbers):
    answer = []
    
    for idx1, num1 in enumerate(numbers):
        for idx2, num2 in enumerate(numbers):
            if idx1 != idx2:
                sum = num1 + num2
                if sum not in answer:
                    answer.append(sum)
    
            
    return sorted(answer)