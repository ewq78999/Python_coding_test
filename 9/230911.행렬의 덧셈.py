def solution(arr1, arr2):
    return [[a + b for a, b in zip(a_horizon, b_horizon)] for a_horizon, b_horizon in zip(arr1, arr2)]

# return[[두 원소를 처리한다 for 가져온 해당행] for 두 행렬의 행을 동시에 가져온다]


# # 만약 두 행렬의 길이가 달라서 오류가 발생한다면 어떻게 해야할까?
# def adjust_matrix_size(arr1, arr2):
#     rows1, rows2 = len(arr1), len(arr2)

#     # arr1(2)의 첫번째 행의 길이( = arr1(2)의 열의 개수) / if를 사용해 행렬이 비어 있으면 열의 갯수를 0으로 설정
#     cols1, cols2 = len(arr1[0]) if arr1 else 0, len(arr2[0]) if arr2 else 0

#     # 작은 행렬에 새로운 행을 추가하며 행의 크기를 맞춤
#     for _ in range(rows1, rows2):
#         arr1.append([0] * cols1)
#     for _ in range(rows2, rows1):
#         arr2.append([0] * cols2)

#     # 작은 행렬에 새로운 열을 추가하며 열의 크기를 맞춤
#     for row in arr1:
#         for _ in range(cols1, cols2):
#             row.append(0)
#     for row in arr2:
#         for _ in range(cols2, cols1):
#             row.append(0)

#     return arr1, arr2

# def solution(arr1, arr2):
#     # 정의한 함수 적용
#     arr1, arr2 = adjust_matrix_size(arr1, arr2)
#     return [[a + b for a, b in zip(a_horizon, b_horizon)] for a_horizon, b_horizon in zip(arr1, arr2)]
