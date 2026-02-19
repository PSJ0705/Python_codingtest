def solution(n):
    ans = 0 
    tmp = n
    while tmp != 0:
        if tmp % 2 == 0:
            tmp = tmp /2
        else :
            tmp -= 1
            ans += 1

    return ans