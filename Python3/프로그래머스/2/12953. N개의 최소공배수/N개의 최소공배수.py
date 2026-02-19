def getGCD(a, b):
    if b == 0:
        return a
    return getGCD(b, a % b)

def solution(arr):    
    for i in range(len(arr)-1):
        box = getGCD(arr[i],arr[i+1])
        arr[i+1] = int((arr[i] * arr[i+1]) / box)       
    answer = arr[-1]
    return answer