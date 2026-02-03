from itertools import permutations

def solution(bablling):
    mask = ['aya', 'ye', 'woo', 'ma']
    cnt = 0
    
    for word in bablling:
        for j in mask:
            if j in word:
                if j+j in word:
                    break
                word = word.replace(j, " ")
        if word.replace(" ","") == "":
            cnt += 1
    return cnt