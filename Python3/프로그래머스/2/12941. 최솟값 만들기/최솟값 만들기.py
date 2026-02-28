def solution(A,B):
    sum = 0
    A.sort(), B.sort()

    for x in range(len(A)):
        sum += A[x] * B.pop()
            

    return sum