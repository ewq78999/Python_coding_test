def solution(sizes):
    max_w = 0
    max_h = 0
    
    for index, (w, h) in enumerate(sizes):
        # w, h  위치 상관없이 가장 긴 길이가 가로가 되야하므로 정렬해준다 
        if w < h:
            w, h = h, w
              # max(적용할 곳, 최솟값)
        max_w = max(max_w, w)
        max_h = max(max_h, h)    
    
    return max_w * max_h