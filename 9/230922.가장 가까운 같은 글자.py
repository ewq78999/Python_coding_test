def solution(s):
    answer = []
    
    for idx, char in enumerate(s):
        # 나를 기준으로 앞에 나온 글자들 비교해야 함
        past_chars = s[:idx]
        if char in past_chars:
            last_char_idx = past_chars.rfind(char)
            answer.append(idx - last_char_idx)
        else:
            answer.append(-1)
            
    return answer