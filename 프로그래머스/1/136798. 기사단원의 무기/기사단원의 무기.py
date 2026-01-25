def solution(number, limit, power):
    numlist = []
    
    for i in range(1,number+1):
        j = 1
        cnt = 0
        while j*j <= i:
            if j*j == i:
                cnt = cnt + 1
            elif i % j == 0:
                cnt += 2
            j += 1
        if cnt > limit:
            cnt = power
        numlist.append(cnt)
    return sum(numlist)