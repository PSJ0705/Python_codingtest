def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0
    i = 0
    j = len(people) -1
    
    while i <= j:
        if people[i] + people[j] <= limit:
            print(people[i], people[j])
            i += 1
            j -= 1
            cnt += 1
        else:
            print(people[i])
            i += 1
            cnt +=1
    
    return cnt