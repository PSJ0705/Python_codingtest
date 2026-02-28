def solution(s):
    box = list(s)
    
    if box[0] == ')' or box[-1] == '()':
        return False
    else:
        cnt = 0
        for i in range(len(box)):
            if cnt < 0:
                break
            elif box[i] == '(':
                cnt += 1
            elif box[i] == ')':
                cnt -= 1
        if cnt == 0:
            return True
        else:
            return False