def solution(price, money, count):
    for i in range(1, count+1):
        money -= price*i
    if money < 0:
        money = abs(money)
    else:
        money = 0
    
    return money

# abs = 절대값 함수, abs(-10) = 10