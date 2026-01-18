def solution(word):
    answer = []
    box = ''
    for i in range(len(word)):
        if word[i] not in box:
            box = box + (word[i])
            answer.append(-1)
        elif word[i] in box:
            print(i - box.rindex(word[i]))
            answer.append(i - box.rindex(word[i]))
            box = box + (word[i])
    print(box)
    print(answer)
    return answer