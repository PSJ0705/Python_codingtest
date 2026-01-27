def solution(s):
    answer = []
    
    box = s.split(" ")
    
    for i in box:
        tmp_word = ""
        for j in range(len(i)):
            if j % 2 == 0 :         
                tmp_word += i[j].upper()
            elif j % 2 == 1:
                tmp_word += i[j].lower()
        answer.append(tmp_word)
    return " ".join(answer)