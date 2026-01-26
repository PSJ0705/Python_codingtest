def solution(num):
    sum = 1
    for i in range(3, num+1,2):
        j = 2
        cnt = 0 
        tmp = int(i ** 0.5)
        while j <= tmp:
            if i % j == 0:      #소수가 아님
                cnt += 1
                break
            j += 1
        if cnt == 0:
            sum += 1
    return sum