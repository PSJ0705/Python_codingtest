def solution(n):
    sum = 0
    while(n>=10):
        num = n % 10
        n = n//10
        sum += num
    sum = sum + n
    print(sum)
    return sum