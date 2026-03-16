def dfs_sol(c_k, cnt, dfs, flag, answer):
    
    answer[0] = max(cnt, answer[0])
    
    for i in range(len(dfs)):
        if not flag[i] and c_k >= dfs[i][0] :
            flag[i] = True
            dfs_sol(c_k - dfs[i][1], cnt+1, dfs, flag, answer)
            flag[i] = False


def solution(k, dfs):
    
    flag = [False] * len(dfs)
    cnt = 0
    answer = [0]
    
    dfs_sol(k, cnt, dfs, flag, answer)
    
    return answer[0]