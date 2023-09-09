def solution(absolutes, signs):
    result = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            result += absolute
        else:
            result -= absolute
            
    return result
            

# zip : 두 리스트들을 짝지어줌, dict(zip())도 가능, 가장 짧은 인자를 기준으로 
# 짝지어지고 나머지는 버려지기 때문에 길이 유의.