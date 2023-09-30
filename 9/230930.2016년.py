# 날짜와 관련된 문제는 datetime을 불러올 것
from datetime import date

def solution(a, b):
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    D = date(2016, a, b)
    
    d = D.weekday()
    
    return days[d]