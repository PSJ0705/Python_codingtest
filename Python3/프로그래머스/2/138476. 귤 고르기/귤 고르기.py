def solution(k, tan):
    box = {}
    sum = 0
    cnt = 0
    
    for value in tan:
        if value in box:
            box[value] += 1
        else:
            box[value] = 1
            
    orange_box = list(box.values())
    orange_box.sort(reverse=True)
    
    for i in orange_box:
        sum += i
        cnt += 1
        if sum >= k:
            break

    return cnt