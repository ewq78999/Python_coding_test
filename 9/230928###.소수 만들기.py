# 소수란 자기자신과 1로만 나눠지는 수, 소수가 될 때마다 count+=1 을 하면 된다
def solution(nums):
    count = 0
    n = sorted(nums)
    l = len(n)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                minor = n[i] + n[j] + n[k]
                # 소수 판별 코드, all 함수를 추가로 공부할 것
                if minor > 1 and all(minor % a != 0 for a in range(2, minor)):
                    count += 1
                    
#                 if minor < 2:
#                     continue
                    
#                 M = True
#                 for a in range(2, minor):
#                     if minor % a == 0:
#                         M = False
#                         break
#                 if M:
#                     count += 1
        

    
    return count