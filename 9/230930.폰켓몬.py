# 연구실에 있는 총 n마리의 폰켓몬 중 n/2마리를 가져가도 좋다
# 최대한 많은 종류의 폰켓몬을 선택하여 종류 갯수 = result 
def solution(nums):
    result = 0
    amount = len(nums)//2
    # set을 사용하여 중복값 제거해라
    n = set(nums)
    
    # 만일 가질 수 있는 최대값인 n/2 보다 set()을 사용했을 때 종류가 작다면...set()한 종류밖에 선택 할 수 없다
    if len(set(nums)) < amount:
        amount = len(set(nums))
        result = amount
    else:
        result = amount
        
    return result

# def solution(nums):
#     return min(len(nums) // 2, len(set(nums)))