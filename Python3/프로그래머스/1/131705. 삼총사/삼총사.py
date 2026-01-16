def solution(num):
    answer = 0
    cnt = 0
    for i in range(len(num) - 2):
        for j in range(i+1, len(num)-1, 1):
            for k in range(j+1, len(num),1):
                answer = num[i] + num[j] + num[k]
                if answer == 0:
                    cnt += 1
                print(f"i값 : {num[i]}, j값 : {num[j]}, k값 {num[k]}, answer : {answer}, cnt : {cnt}")
            answer = 0
    print(f"CNT는 {cnt}")
    return cnt