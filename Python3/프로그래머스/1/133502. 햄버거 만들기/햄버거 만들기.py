def solution(ingre):
    answer = 0
    sample = [1,2,3,1]
    box = []
    
    for i in ingre:
        box.append(i)
        if box[-4:] == [1,2,3,1]:
            answer += 1
            for j in range(4):
                box.pop()

    return answer