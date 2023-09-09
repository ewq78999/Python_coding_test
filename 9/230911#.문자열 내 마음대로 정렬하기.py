def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])

# sorted 는 리스트 내의 객체를 정렬하여 변환시키는 기능
# sorted(strings)로 전체 문자열을 기준으로 정렬 후(입출력 예2) 다시 한번 sorted로 묶어 n번째 글자를 기준을 정렬(입출력 예1) 
# lambda(일회성 간단한 함수 생성) x: x[n] 은 문자열 x를 받아 n번째 글자를 반환하라는 의미

# ex) n=1 & ['sun', 'bed', 'car'] => ['car', 'bed', 'sun'] 
# => ['car', 'bed', 'sun'](이때 문자열은 0부터 시작하므로 문자의 1번째 글자인 'a', 'e', 'u'를 기준을 정렬한다)

# sort / sorted 차이 
# sort => 원본 리스트 값 정렬 & return 없음 / sorted => 원본 리스트 값 유지되고 새 리스트에 저장, 따라서 리턴 있음