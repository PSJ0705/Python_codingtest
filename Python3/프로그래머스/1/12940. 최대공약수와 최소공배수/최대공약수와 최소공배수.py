def gcd(n,m):   #최대 공약수
    while m > 0:
        n,m = m, n%m
    return n

def solution(n, m):
    answer = []
    G = gcd(n,m)    #최대공약수
    answer.append(G)
    L = (n / G) * (m / G) * G   #최소공배수
    answer.append(L)
    print("최대공약수 : " + str(answer[0]), "최소공배수 : " + str(answer[1]))
    
    return answer