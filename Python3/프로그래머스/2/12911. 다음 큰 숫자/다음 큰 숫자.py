def solution(n):
    tmp = n+1
    flag = True
    
    while flag:
        if format(tmp,'b').count('1') == format(n,'b').count('1'):
            flag = False
        else:
            tmp += 1
    return tmp