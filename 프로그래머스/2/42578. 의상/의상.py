def solution(clothes):
    answer = 0
    cnt = 0
    gear_count = {}
                
    for i in clothes:
        kind = i[1]
        if kind in gear_count:
            gear_count[kind] = gear_count[kind] + 1
        else:
            gear_count[kind] = 2
            
    print(gear_count)
    
    x = 1
    
    for value in gear_count.values():
        x = x * value

 

    return x - 1 