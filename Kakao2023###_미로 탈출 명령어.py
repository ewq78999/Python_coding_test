# (x,y) =k=> (r,c)
def solution(n, m, x, y, r, c, k):
    # 이동할 수 없으면 impossible return
    # 이동할 수 있으면 가장 빠른 경로로 탈출
    # 1. k가 부족한 경우
    distance = abs(r - x) + abs(c - y)
    if distance > k:
        return "impossible"
    # 2. k가 후퇴 후 전진할 때 짝이 맞지 않는 경우_k=2 인데 1칸만 가야할 때
    if (k - distance) % 2 != 0:
        return "impossible"
    # 3. 조건에 충족될 경우
    # dlru 사전순 / d:down, l:left, r:right, u:up 
    down = max(r - x, 0)
    left = max(y - c, 0)
    right = max(c - y, 0)
    up = max(x - r, 0)
    pair = (k - distance) // 2
    answer = ''
    for _ in range(k):
        # 그냥 가거나 or 되돌아 갈 때
        if (down or pair) and x < n:
            answer += 'd'
            # 그냥 갈 때
            if down:
                down -= 1
            # 되돌아 갈 때
            else: 
                pair -= 1
                up += 1
            # 현재좌표 표시
            x += 1
        elif (left or pair) and y > 1:
            answer += 'l'
            # 그냥 갈 때
            if left:
                left -= 1
            # 되돌아 갈 때
            else: 
                pair -= 1
                right += 1
            # 현재좌표 표시
            y -= 1
        elif (right or pair) and y < m:
            answer += 'r'
            # 그냥 갈 때
            if right:
                right -= 1
            # 되돌아 갈 때
            else: 
                pair -= 1
                left += 1
            # 현재좌표 표시
            y += 1
        else:
            answer += 'u'
            if up:
                up -= 1
            else:
                pair -= 1
                down += 1
            # 현재좌표 표시
            x -= 1

    return answer