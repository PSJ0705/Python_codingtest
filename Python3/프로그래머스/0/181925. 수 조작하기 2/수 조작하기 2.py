def solution(numLog):
    answer = ''
    for i in range(len(numLog)):
        if i == 0:
            num = ''
        num = numLog[i] - numLog[i-1]
        if i != 0:
            if num == 1:
                answer += "w"
            elif num == -1:
                answer += "s"
            elif num == 10:
                answer += "d"
            else:
                answer += "a"
    return answer