def solution(clothes):
    answer = 0
    cnt = 0
    gear_count = {}
                
    for i in clothes:
        kind = i[1]
        gear_count[i[1]] = gear_count.get(i[1],1) + 1
            
    print(gear_count)
    
    x = 1
    
    for value in gear_count.values():
        x = x * value

 

    return x - 1 