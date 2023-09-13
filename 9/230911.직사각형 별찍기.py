n, m = map(int, input().split())
for i in range(m):
    print('*' * n)
    

# 다른 풀이 방법

# answer = (('*'*n + '\n')*m)
# print(answer)

# n, m = map(int, input().split())
# print('\n'.join(['*' * n for _ in range(m)]))
# 줄바꿈을 해주는 '\n'을 ['*' * n for _ in range(m)]가 끝날 때마다 join 시켜준다