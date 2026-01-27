def solution(nums):
    import itertools
    import math
    
    box = list(itertools.combinations(nums,3))
    cnt = 0
    
    for i in box:
        total = sum(i)
        tmp = total ** 0.5
        j = 2
        while j <= tmp:
            if total % j == 0:
                break
            j += 1
        else:
            cnt += 1
    return cnt