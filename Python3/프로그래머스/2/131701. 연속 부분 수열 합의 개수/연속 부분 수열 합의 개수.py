def solution(num):
    box = []
    num_len = len(num)     
    test = num * 2
    test_len = len(test)

    for i in range(num_len):
        for j in range(i+1,i+num_len+1):
            box.append(sum(test[i:j]))
           
    total = list(set(box))
    
    return len(total)