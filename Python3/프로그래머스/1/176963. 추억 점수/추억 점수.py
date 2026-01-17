def solution(name, score, photo):
    answer = []
    photo_score = 0
    photo_dict = dict(zip(name,score))
    for i in photo:
        for j in i:
            if j in name:
                photo_score += photo_dict.get(j)
        answer.append(photo_score)
        photo_score = 0
    return answer