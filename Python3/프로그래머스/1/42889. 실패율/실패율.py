def solution(N, stages):
    stage_count = []        #스테이지 별 플레이어의 수
    player = len(stages)    #전체 플레이어의 수
    fail_count = []         #실패율
    cnt = 1
    
    while cnt <= N:             
        stage_count.append(stages.count(cnt))
        cnt += 1
        if cnt > N:
            stage_count.append(stages.count(cnt))
            
    for i in range(len(stage_count)):
        fail_player = stage_count[i]
        
        if player == 0:
            fail_count.append(0)
            continue
            
        fail_count.append(fail_player/player)
        
        if fail_player != 0:
            player = player - fail_player
    
    pairs = [(i+1, fail_count[i]) for i in range(N)]  
    pairs.sort(key=lambda x:(-x[1], x[0]))
    
    answer = [stage for stage,_ in pairs]
    
    print(answer)
    
    return answer



