def solution(s):
    box = []
    
    for char in s:
        if box and box[-1] == char:
            box.pop()
        else:
            box.append(char)
            
    if box:
        return 0
    else:
        return 1
    