def solution(s, n):
    answer = ''
    # 문자의 아스키 코드를 얻는 법: ord() / 그 코드 값을 다시 문자로 변환하는 법: chr()
    # range는 정수값을 기대하므로 result = string 형식인 경우 사용하기 힘듬
    
    # for idx, char in enumerate(s):
    for char in s:
        # 알파벳은 대문자, 소문자 각각 26글자여서 'Z' 다음 'A'로 돌아와야 되기 때문에
        
        # chr(ord(char) - ord('A') + n) % 26 + ord('A')) 형식으로 진행해야 함
        
        # !!!!!! 그냥 외워라_시저 암호 !!!!!!!
        
        # 대문자인 경우
        if 'A' <= char <= 'Z':
                    # (0 - 2('A') + 1(n)) % 26 = 3 / 3 + 2 = 5 / chr(5)
            answer += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        # 소문자인 경우
        elif 'a' <= char <= 'z':
            answer += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        # 공백인 경우
        else:
            answer += char
    
    return answer