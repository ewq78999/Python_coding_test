def solution(s):
    answer = ''
    l = len(s)

    for index, char in enumerate(s):
        if l % 2 == 1 and index == l // 2:
            answer = char
            break
        elif l % 2 == 0 and (index == l // 2 - 1 or index == l // 2):
            answer += char

    return answer