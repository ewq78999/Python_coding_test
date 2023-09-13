def solution(food):
    # ''.join((food 원소값을 글자로) * (index // 2 해서 소수점 버리고 남은 수) for food, index in enumerate(food) )
    first = ''.join(str(food) * (index // 2) for food, index in enumerate(food))
    # 오른쪽 선수가 먹은 음식 추가(역순으로)
    second = first[::-1]
    # 중앙에 물 추가
    answer = first + '0' + second

    return answer

# def solution(food):
#     # food 첫번째에 위치한 물을 제외하고 한 선수가 먹을 음식 양 (/2 필요)
#     total = sum(food[1:]) // 2

#     answer = []  # 결과를 저장할 리스트
#     idx = 1  # 현재 먹을 음식의 인덱스. 물을 제외해야 되기 때문에 idx = 0 부터 시작하지 않음

#     # 아직 한 선수가 먹어야 할 음식의 양이 남아 있고 idx가 len(food)보다 작다면(list out of range 방지)
#     while total > 0 and idx < len(food):
#         # 현재 음식 양의 절반
#         half_food = food[idx] // 2
#         # 현재 음식의 양의 절반이 total보다 작거나 같다면 해당 음식을 그만큼 추가
#         if half_food <= total:
#             answer.extend([str(idx)] * half_food)
#         # 먹은 음식의 양을 감소시킴
#             total -= half_food
#             food[idx] -= half_food
#         # 현재 음식의 양의 절반이 total보다 크다면 total만큼만 해당 음식을 추가
#         else:
#             answer.extend([str(idx)] * total)
#             total = 0
        
#         # 다음 순서로 넘어감
#         idx += 1

#     # 중앙에 물 배치
#     answer.append('0')
#     # 오른쪽 선수가 먹는 음식의 순서 추가(처음부터 마지막 바로 앞 원소까지, 역순으로)
#     answer.extend(answer[:-1][::-1])
#     # join을 사용해 문자열을 하나로 합침
#     return ''.join(answer)


# def solution(food):
#     answer = ''
#     # answer의 중간지점 index 번호
#     mid_idx = 0
#     for i in range(1,len(food)):
#         # 한쪽에 채워야할 i번 음식 개수
#         num_food = food[i]//2
#         # answer의 중간 지점에 "i"를 i 음식 개수의 2배를 넣는다. (양쪽 집어넣어야하니깐)
#         answer = answer[:mid_idx] + str(i) * num_food * 2 + answer[mid_idx:]
#         # 중간지점 index 갱신
#         mid_idx += num_food
#     # 마지막으로 물 넣기
#     answer = answer[:mid_idx] + "0" + answer[mid_idx:]

#     return answer


# def solution(food):
#     answer = ''
#     for i in range(1,len(food)):
#         answer += str(i) * (food[i]//2)

#     answer_reverse = answer[::-1]
#     answer = answer + '0' + answer_reverse

#     return answer