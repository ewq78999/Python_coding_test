def solution(arr):
    # 우선 arr 배열에서 첫 번째 원소는 무조건 포함되게 answer [] 생성
    answer = [arr[0]]

    # arr의 두 번째 원소부터 마지막 원소까지 반복
    for i in range(1, len(arr)):
        # 이전 위치의 원소와 현재 원소가 다르면 answer에 추가
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer