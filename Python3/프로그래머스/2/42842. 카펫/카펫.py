def solution(brw, ylw):
    box_size = brw + ylw
    num = []
    answer = []
    
    for i in range (1,box_size+1):
        if (box_size % i == 0):
            num.append(i)
    
    if len(num) % 2 != 0:
        num_len = len(num) // 2
        a_box = num[num_len:]
        b_box = num[:num_len+1]
    else:
        num_len = len(num) // 2
        a_box = num[num_len:]
        b_box = num[:num_len]
    
    a_box.reverse()
            
    for x in a_box:
        for y in b_box:
            if (2 * (x + y) - 4 == brw and x * y == box_size):
                answer.append(x)
                answer.append(y)
              
    
    return answer