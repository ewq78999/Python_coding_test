def solution(s):
    return len(s) in [4,6] and s.isdigit() 

# .isdigit()를 사용하면 문자열이 숫자로만 구성되어 있는지 확인할 수 있다
# .isalpha()를 사용하면 문자열이 글자로만 구성되어 있는지 확인할 수 있다