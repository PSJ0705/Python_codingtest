def solution(k, m, score):
    total = 0
    score.sort(reverse=True)
    apple = [score[i:i + m] for i in range(0,len(score), m)]
    for i in apple:
        if len(i) >= m:
            total = total + (min(i) * m) 
        else:
            return total
    return total