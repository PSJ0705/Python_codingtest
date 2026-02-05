def solution(ingre):
    answer = 0
    sample = [1,2,3,1]
    box = []
    i = 0
    
    while i <= len(ingre):
        j = i
        box.append(ingre[i:i+4])
        if sample in box:
            del ingre[i:i+4]
            box = []
            answer += 1
            i = j - 4
            continue
        else:
            box = []
            i += 1
    return answer