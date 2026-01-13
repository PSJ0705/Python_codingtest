def solution(s):
    answer = 0
    seq = s.split(" ")
    for i in range(len(seq)):
        if seq[i] != 'Z':
            answer = answer + int(seq[i])
        else:
            answer = answer - int(seq[i-1])
    return answer