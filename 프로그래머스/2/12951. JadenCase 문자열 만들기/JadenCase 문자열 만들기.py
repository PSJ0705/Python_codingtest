def solution(s):
    answer = []
    box = s.lower()
    check = True
    
    for word in box:
        if word == ' ':
            check = True

        elif check == True:
            word = word.upper()
            check = False
            
        answer.append(word)   
        
    answer = ''.join(answer)
  
    return answer