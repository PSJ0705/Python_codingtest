def solution(n):
    box = []
    cnt = 0
    
    for x in range(1,n+1):
        box.append(x)
    
    for i in range(len(box)):
        tmp = 0
        for j in range(i, len(box)):
            tmp = sum(box[i:j])
            if tmp == n:
                cnt += 1
                break
            elif tmp > n:
                break
                
    return cnt + 1