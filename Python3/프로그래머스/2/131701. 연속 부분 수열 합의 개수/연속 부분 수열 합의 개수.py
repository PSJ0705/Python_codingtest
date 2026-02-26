def solution(num):
    num_len = len(num)
    test = num * 2  
    box = set()     

    for i in range(num_len):
        current_sum = 0

        for j in range(i, i + num_len):
            current_sum += test[j]
            box.add(current_sum)

    return len(box)