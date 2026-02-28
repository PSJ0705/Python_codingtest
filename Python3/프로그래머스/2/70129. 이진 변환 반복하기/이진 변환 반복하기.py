def solution(s):
    answer = []
    cnt = 0
    tmp_cnt = 0
    
    while s != '1':   
        for x in s:
            if x == '0':
                s = s.replace('0','')
                tmp_cnt += 1
        s_len = len(s)              
        s = format(s_len,'b')       
        cnt += 1                    

    answer = [cnt, tmp_cnt]
    
    
    return answer