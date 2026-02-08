def solution(s):
    box = list(map(int, s.split()))
    min_num = min(box)
    max_num = max(box)
    
    return str(min_num) + ' ' +  str(max_num)