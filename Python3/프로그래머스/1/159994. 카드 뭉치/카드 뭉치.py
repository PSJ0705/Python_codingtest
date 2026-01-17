def solution(cards1, cards2, goal):
    answer = ''
    k = j = 0
    for i in range(len(goal)):
        if j < len(cards1) and goal[i] == cards1[j]:
            j += 1
        elif k < len(cards2) and goal[i] == cards2[k]:
            k += 1
        else : 
            return "No"
    return "Yes"